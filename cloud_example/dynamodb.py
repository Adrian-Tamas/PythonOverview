import boto3
import logging
import polling2

from typing import List, Dict, Any

from assertpy import assertpy

from utils.lists import slice_list

logger = logging.getLogger('cloudrunner-automation')


class DynamoDBHandler:
    def __init__(self, table_name: str, table_region: str):
        """
        :param table_name: name of the dynamodb table
        :param table_region: name of the AWS region of the dynamodb table; e.g., us-east-1
        """
        self._table_name = table_name
        self._table_region = table_region
        self._dynamodb = boto3.resource("dynamodb", region_name=table_region)
        self._table = self._dynamodb.Table(self._table_name)

    def _batch_get_item(self, pk_values):
        response = self._dynamodb.batch_get_item(
            RequestItems={self._table_name: {"ConsistentRead": True, "Keys": pk_values}}
        )
        return response

    def batch_get_item(self, pk_values: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
          pk_values: list of primary keys of the items we want to get from the
            table; each primary key has to follow the format:
              {pk_attribute_name: pk_value}
            If you have a composite key, then the pk should be specified as
              {pk_attribute1_name: pk_attr1_value, pk_attribute2_name: pk_attr2_value}

        Returns:
          a list of records; each record is a dict, its keys are attribute names
          and the values are attribute values.
        """
        items = []
        # the boto3 client enforces a limit of 100 items per request to its
        # batch_get_item method, hence this for-loop with this particular
        # slice_size
        for pk_chunk in slice_list(pk_values, slice_size=100):
            response = self._batch_get_item(pk_chunk)
            items.extend(response["Responses"][self._table_name])
            # the dynamodb API restricts the size of its (batch get item) responses
            # to 1MB or less; if that limit is exceeded, dynamodb will return a
            # subset of the requested elements, and report back the pks of the
            # elements it didn't return in the 'UnprocessedKeys' entry; the loop
            # below keeps fetching data until there are no records pending in
            # UnprocessedKeys.
            #
            # NOTE: the loop should always finish, since dynamodb also enforces a
            # limit of 400KB on each record
            while response["UnprocessedKeys"]:
                pk_chunk = response["UnprocessedKeys"][self._table_name]["Keys"]

                response = self._batch_get_item(pk_chunk)
                items.extend(response["Responses"][self._table_name])
        return items

    def batch_write_items(self, items_data: List[Dict[str, Any]]):
        with self._table.batch_writer() as batch:
            for item in items_data:
                batch.put_item(Item=item)

    def batch_delete_items(self, items_data: List[Dict[str, Any]]):
        with self._table.batch_writer() as batch:
            for item in items_data:
                batch.delete_item(Key=item)

    def ensure_items_are_in_the_database(self, pk_values: List[Dict[str, Any]]):
        try:
            polling2.poll(lambda: len(self.batch_get_item(pk_values=pk_values)) > 0, step=5, timeout=120)
        except polling2.TimeoutException:
            assertpy.fail(f"Unable to find items in the DynamoDB by searching using {pk_values}")

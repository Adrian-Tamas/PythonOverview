from behave import given, when, then
from assertpy import assert_that


@given('I have the number {num:d}')
def have_number(context, num):
    if not hasattr(context, 'numbers'):
        context.numbers = []
    context.numbers.append(num)


@when('I add the numbers together')
def add_numbers(context):
    context.result = sum(context.numbers)


@then('the result should be {expected_result:d}')
def check_result(context, expected_result):
    assert_that(context.result).is_equal_to(expected_result)

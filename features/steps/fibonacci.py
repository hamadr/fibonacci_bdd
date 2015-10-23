from behave import *
from maths.fibonacci import fibonacci

@given(u'I want the number {number} fibonacci number')
def step_impl(context, number):
    context.number = int(number)

@when(u'I launch fibonacci function')
def step_impl(context):
    context.result = fibonacci(context.number)

@then(u'I get {number}')
def step_impl(context, number):
    assert context.result == int(number)

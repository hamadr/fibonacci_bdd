from behave import *

@given(u'I want the number (\d*) fibonacci number')
def step_impl(context, number):
        raise NotImplementedError(u'STEP: Given I want the number' + number + ' fibonacci number')

@when(u'I launch fibonnaci function')
def step_impl(context):
        raise NotImplementedError(u'STEP: When I launch fibonnaci function')

@then(u'I get (\d*)')
def step_impl(context, number):
        raise NotImplementedError(u'STEP: Then I get ' + number)

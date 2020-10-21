from django import template

register = template.Library()

@register.filter(name='cutit')
def cutit(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, ' replaced text ')

# register.filter('to_cut',cut)

@register.filter(name='multi')
def multi(number,arg):
    return number*arg

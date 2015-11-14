from django import template
 
register = template.Library()
 
class Counter:
    count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def double(self):
        self.count *= 2
         
class SetVarNode(template.Node):
 
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value
 
    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context.dicts[0][self.var_name] = value
        return u""
 
def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])
 
register.tag('set', set_var)
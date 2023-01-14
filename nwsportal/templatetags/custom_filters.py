from django import template


register = template.Library()




# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(message: str):
   """
   value: значение, к которому нужно применить фильтр
   """
   variants = ['mat', 'abc', 'def', 'no', 'filter']
   ln = len(variants)
   filtred_message = ''
   string = ''
   pattern = '*'
   for i in message:
       string += i
       string2 = string.lower()

       flag = 0
       for j in variants:
           if not string2 in j:
               flag += 1
           if string2 == j:
               filtred_message += pattern * len(string)
               flag -= 1
               string = ''

       if flag == ln:
           filtred_message += string
           string = ''

   if string2 != '' and string2 not in variants:
       filtred_message += string
   elif string2 != '':
       filtred_message += pattern * len(string)

   return filtred_message

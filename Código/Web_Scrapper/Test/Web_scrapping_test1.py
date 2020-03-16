from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://stackoverflow.com/questions/9333245/python-printing-text-after-printing-a-variables')
#print('Esto es lo que devuelve el read: {}'.format(html.read()))
bsObj=BeautifulSoup(html.read())
question_array = bsObj.find('div',{'class':'postcell'})
question_test =question_array.find('div',{'class':'post-text'}) 
print('Esto es lo que hemos rescatado: {}'.format(question_array))
print('\n\n----------------------------\n\nEsta es la pregunta:\n{}\n\n'.format(question_test.get_text()))
answer_array = bsObj.find('div',{'class':'answercell'})
print('\n\n----------------------------\n\nEsta es la respuesta:\n{}\n\n'.format(answer_array.get_text()))



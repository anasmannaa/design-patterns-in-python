#This module is not part of the memento design pattern.
#It is just for you to run and test the pattern workin
import document_state
import document
import history

document = document.Document()
history = history.History()

document.set_content("demo content")
document.set_font_name("Helvatica")
document.set_font_size(12)
history.push(document.create_state())
print(document)

document.set_content("2nd version of content")
document.set_font_name("Helvatica")
document.set_font_size(22)
history.push(document.create_state())
print(document)

document.set_content("3nd version of content")
document.set_font_name("Tahoma")
print(document)

document.restore(history.pop())
print(document)

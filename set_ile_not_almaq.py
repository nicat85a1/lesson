"""
# yöntem 1

file = open("C:/Users/user/Desktop/python/Source-code_editor.txt","r") # dosyayı oku
liste = file.readlines() # dosya içeriğini liste'ye aktar
liste = [satir.strip() for satir in liste] # strip ile boşlukları temizle
liste = list(set(liste)) # sort uygulamak için set'i list içerisine aldım
liste.sort() # incelemeyi kolaylaştırmak için alfabe sırasıyla yazdırdım
print(liste) # finiş
file.close()
"""

"""
# yöntem 2 ( sort -> sorted )

listx = set() # set oluşturdum

with open('C:/Users/user/Desktop/python/Source-code_editor.txt', 'r') as dosya: # dosyayı okutuyorum
    for satir in dosya: # for ile dosya'dan verilere erişim
        ide = satir.strip() # strip ile boşluk temizleme
        listx.add(ide) # verileri set'e ekledim
sorted_listx = sorted(listx) #sorted ile set'i sıralı bir listeye dönüştürüyoruz
print(sorted_listx) # finiş

# çıktı

"""
['AWS Cloud 9', 'Android Studio', 'Aptana Studio', 'Aptana Studio 3', 'Asana', 'Atom', 'AutoHotkey', 'Bluefish', 'Brackets', 'Coda', 'CodeStream', 
'CoffeeCup HTML Editor', 'DeskTime', 'Eclipse', 'Emacs', 'GNU Emacs', 'Geany', 'Gedit', 'GitHub Copilot', 'InteliJ IDEA', 'IntelliJ IDEA', 'Jam', 
'Jira', 'JupyterLab', 'Komodo Edit', 'MantisBT', 'Mermaid JS', 'Microsoft Visual Studio', 'NetBeans', 'Notepad++', 'PHPStorm', 'Phase 5', 'PhpStore', 
'Pieces', 'PlainEdit.NET', 'Plaky', 'Programmer’s Notepad', 'PyCharm', 'Slack', 'SlickEdit', 'SmartTask', 'Sublime Text', 'Sublime Text 2', 'SynWrite', 
'Syncfusion', 'Tabnine', 'TextMate', 'The Silver Searcher', 'Toby', 'Tuple', 'UltraEdit', 'Vim', 'Visual Studio', 'Visual Studio Code', 'WebStorm', 
'WebWork', 'Xcode', 'Zenhub', 'dbForge SQL Complete', 'iTerm', 'jEdit'] # sort işlemi ile çıktı

"""

# sorunlu çıktılar

# 'Brackets\u200b'
# 'Notepad++\u200b'
# 'Sublime Text\u200b'

"""

# dosya içerisinde kodların çalışma mantığı:

"""
list1 = ["Atom","Brackets","Eclipse","Emacs","Gedit","NetBeans","Notepad++","SlickEdit","Sublime Text","TextMate","UltraEdit","Vim","Visual Studio Code"]
list2 = ["Brackets","Notepad++","Visual Studio Code","Sublime Text","Atom","Vim","Coda","UltraEdit","Bluefish","Komodo Edit"]
list3 = ["Phase 5","Programmer’s Notepad","SynWrite","PlainEdit.NET","jEdit","Sublime Text 2","Brackets","Aptana Studio 3","Sublime Text","Visual Studio Code"]
list4 = ["CodeStream","IntelliJ IDEA","Sublime Text","GitHub Copilot","Tabnine","JupyterLab","dbForge SQL Complete","Jira","MantisBT","Jam","The Silver Searcher",
         "Asana","SmartTask","Zenhub","Plaky","DeskTime","WebWork","Tuple","AutoHotkey","Slack","Pieces","Toby","Mermaid JS","iTerm"]
list5 = ["WebStorm","Syncfusion","NetBeans","AWS Cloud 9","Visual Studio","IntelliJ IDEA","Eclipse","PhpStore","Xcode","Microsoft Visual Studio","Android Studio",
         "Xcode","Eclipse","InteliJ IDEA"]
list6 = ["Android Studio","Microsoft Visual Studio","Eclipse","InteliJ IDEA","Xcode"]
list7 = ["Brackets","Sublime Text","Notepad++","Visual Studio Code"]
list8 = ["UltraEdit","Atom","Brackets","Notepad++","Sublime Text","Vim","GNU Emacs","TextMate","Geany"]
list9 = ["Android Studio","Brackets","Xcode","Eclipse","Visual Studio Code","Sublime Text","Atom","Notepad++","CoffeeCup HTML Editor","TextMate","Bluefish","Vim"]
list10 = ["Aptana Studio","PHPStorm","PyCharm","NetBeans","IntelliJ IDEA"]

listx = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10))
listx.sort()
print(listx)

"""
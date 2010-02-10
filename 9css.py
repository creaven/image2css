#!/usr/bin/python

f=open('/Users/moro/tmp/result.css', 'w')

cls='mif-menu-bg'
ie6='.ie6'


coords=(45, 35, 45, 45)

left, top, right, bottom = map(str, coords)

padding_left='40'
padding_top='47'
l='-19'
t='-17'

img='../images/bg-'
ext='png'

imgs={
	"tl": img+'tl'+'.'+ext,
	"tr": img+'tr'+'.'+ext,
	"bl": img+'bl'+'.'+ext,
	"br": img+'br'+'.'+ext,
	"t": img+'t'+'.'+ext,
	"b": img+'b'+'.'+ext,
	"l": img+'l'+'.'+ext,
	"r": img+'r'+'.'+ext,
	"c": img+'c'+'.'+ext
}

css=''
css+='.'+cls+', .'+cls+' div{\n'+'position: absolute;\n'+'overflow:hidden;\n'+'}\n'
css+='.'+cls+' {\n'+'left:'+l+'px;\n'+'top:'+t+'px;\n'+'padding-left:'+padding_left+'px;\n'+'padding-top:'+padding_top+'px;\n'+'}\n'
#css+=ie6+' '+'.'+cls+' {\n'+'overflow-y:hidden;\n'+'}\n'
css+='.'+cls+' .top{\n'+'height: '+top+'px;\n'+'width: 100%;\n'+'position: relative;\n'+'top:-'+padding_top+'px;\n'+'padding-left:'+padding_left+'px;\n'+'padding-top:'+padding_top+'px;\n'+'left:-'+padding_left+'px;\n'+'}\n'
css+='.'+cls+' .center{\n'+'height: 100%;\n'+'width: 100%;\n'+'position: relative;\n'+'top:-'+str(int(bottom)+int(top)+2*int(padding_top))+'px;\n'+'padding-left:'+padding_left+'px;\n'+'padding-top:'+padding_top+'px;\n'+'left:-'+padding_left+'px;\n'+'}\n'
css+='.'+cls+' .bottom{\n'+'height: '+bottom+'px;\n'+'width:100%;\n'+'top:-'+str(int(bottom)+int(top)+2*int(padding_top))+'px;\n'+'position:relative;\n'+'padding-left:'+padding_left+'px;\n'+'left:-'+padding_left+'px;'+'}\n'
css+='.'+cls+' .tl{\n'+'width: '+left+'px;\n'+'height: '+top+'px;\n'+'background:'+'url("'+imgs['tl']+'")'+';\n'+'left:0px;\n'+'top:0px;\n'+'}\n'
css+='.'+cls+' .tr{\n'+'width: '+right+'px;\n'+'height: '+top+'px;\n'+'float:right;\n'+'position: relative;\n'+'background:'+'url("'+imgs['tr']+'");\n'+'top:-'+padding_top+'px;\n'+'}\n'
css+='.'+cls+' .t{\n'+'height: '+top+'px;\n'+'width:100%;\n'+'left:-'+str(int(right)+int(padding_left))+'px;\n'+'top: 0;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right)+int(padding_left))+'px);\n'+'background:'+'url("'+imgs['t']+'")'+';\n'+'padding-left:'+padding_left+'px;\n'+'}\n'
css+=ie6+' '+'.'+cls+' .t{\n'+'left:-'+right+'px;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right))+'px);\n'+'}\n'
css+='.'+cls+' .bl{\n'+'width: '+left+'px;\n'+'height: '+bottom+'px;\n'+'background:'+'url("'+imgs['bl']+'");\n'+'left:0px\n'+'}\n'
css+='.'+cls+' .br{\n'+'width: '+right+'px;\n'+'height: '+bottom+'px;\n'+'float: right;\n'+'position: relative;\n'+'background:'+'url("'+imgs['br']+'")'+';\n'+'}\n'
css+='.'+cls+' .b{\n'+'height: '+bottom+'px;\n'+'width:100%;\n'+'left:-'+str(int(right)+int(padding_left))+'px;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right)+int(padding_left))+'px);\n'+	'background:'+'url("'+imgs['b']+'");\n'+'padding-left:'+padding_left+'px;\n'+'}\n'
css+=ie6+' '+'.'+cls+' .b{\n'+'left:-'+right+'px;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right))+'px);\n'+'}\n'
css+='.'+cls+' .l{\n'+'height:10000px;\n'+'width:'+left+'px;\n'+'left:0;\n'+'top:'+str(int(top)+int(bottom))+'px;\n'+'background:'+'url("'+imgs['l']+'")'+';\n'+'}\n'
css+='.'+cls+' .r{\n'+'height:10000px;\n'+'width:'+right+'px;\n'+'top:'+str(int(top)+int(bottom)-int(padding_top))+'px;\n'+'float:right;\n'+'position:relative;\n'+'background:'+'url("'+imgs['r']+'")'+';\n'+'}\n'
css+='.'+cls+' .c{\n'+'height: 10000px;\n'+'width:100%;\n'+'left:-'+str(int(right)+int(padding_left))+'px;\n'+'top:'+str(int(top)+int(bottom))+'px;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right)+int(padding_left))+'px);\n'+'background:'+'url("'+imgs['c']+'");\n'+'padding-left:'+padding_left+'px;\n'+'}\n'
css+=ie6+' '+'.'+cls+' .c{\n'+'left:-'+right+'px;\n'+'clip:rect(auto auto auto '+str(int(left)+int(right))+'px);\n'+'}\n'


f.write(css)
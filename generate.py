#!/usr/bin Python3

import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(f'{main_url}/{url}')
    soup = BeautifulSoup(response.content)
    return soup

def write_html(title_text,main):
    head = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title></title>
    <link rel="stylesheet" href="../css/basic.css" type="text/css">
    <link rel="stylesheet" href="../css/pygments.css" type="text/css">
    <link href="../css/index.css" rel="stylesheet">
    <style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
    #MathJax_About.MathJax_MousePost {outline: none}
    .MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 5px 0px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 5px; -webkit-border-radius: 5px; -moz-border-radius: 5px; -khtml-border-radius: 5px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
    .MathJax_MenuItem {padding: 1px 2em; background: transparent}
    .MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
    .MathJax_MenuActive .MathJax_MenuArrow {color: white}
    .MathJax_MenuArrow.RTL {left: .5em; right: auto}
    .MathJax_MenuCheck {position: absolute; left: .7em}
    .MathJax_MenuCheck.RTL {right: .7em; left: auto}
    .MathJax_MenuRadioCheck {position: absolute; left: .7em}
    .MathJax_MenuRadioCheck.RTL {right: .7em; left: auto}
    .MathJax_MenuLabel {padding: 1px 2em 3px 1.33em; font-style: italic}
    .MathJax_MenuRule {border-top: 1px solid #DDDDDD; margin: 4px 3px}
    .MathJax_MenuDisabled {color: GrayText}
    .MathJax_MenuActive {background-color: #606872; color: white}
    .MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
    .MathJax_ContextMenu:focus {outline: none}
    .MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
    #MathJax_AboutClose {top: .2em; right: .2em}
    .MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
    .MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
    .MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
    .MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
    .MathJax_MenuClose:hover span {background-color: #CCC!important}
    .MathJax_MenuClose:hover:focus {outline: none}
    </style>
    <style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
    </style>
    <style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
    .MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
    </style>
    <style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
    #MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
    #MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
    #MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
    </style>
    <style type="text/css">.MathJax_Preview {color: #888}
    #MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
    #MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
    .MathJax_Error {color: #CC0000; font-style: italic}
    </style>
</head>
  <body>'''
    tail = '''</body></html>'''
    with open(f'./html/{title_text}.html','w') as html:
        html.write(f'{head}\n{main}\n{tail}')

main_url = 'https://pandas.pydata.org/pandas-docs/stable/reference'
main_soup = get_soup('index.html')
indexes_json = pd.DataFrame(columns=['t','d','p'])
for chapter in main_soup.select('.nav>li>a'):
    print(f"{chapter['href']}\t{chapter.text}")
    chapter_soup = get_soup(chapter["href"])
    for method in chapter_soup.select('tr'):
        title,description = method.select('td')
        description_text = description.p.text
        title_text = title.a['title']
        title_url = title.a['href']

        method_soup = get_soup(title_url)
        main = method_soup.find('div', {'class':'section'})
        write_html(title_text,main)
        indexes_json.loc[title_text] = [title_text,description_text,title_url]
indexes_json.to_json('./indexes.json',orient='records')
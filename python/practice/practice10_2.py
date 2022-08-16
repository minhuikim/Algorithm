### pip install
# pypi
# python.exe -m pip install --upgrade pip
# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''
<p>
 Some
 <b>
  bad
  <i>
   HTML
  </i>
 </b>
</p>
'''

# pip list 현재 설치된 pip list
'''
Package              Version
-------------------- -----------
beautifulsoup4       4.11.1     
pip                  22.2.2     
setuptools           58.1.0
soupsieve            2.3.2.post1
types-beautifulsoup4 4.11.4
'''

# pip show beautifulsoup4 패키지 정보 확인 및 업그레이드 정보
'''
Name: beautifulsoup4
Version: 4.11.1
Summary: Screen-scraping library
Home-page: https://www.crummy.com/software/BeautifulSoup/bs4/
Author: Leonard Richardson
Author-email: leonardr@segfault.org
License: MIT
Location: c:\users\ap1\appdata\local\programs\python\python310\lib\site-packages
Requires: soupsieve
Required-by:
'''

# pip install --upgrade beautifulsoup4 패키지 업그레이드

# pip uninstall beautifulsoup4 패키지 삭제
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parent.parent
D={
'직접 만들며 배우는 코딩 | 코드빚다':'Learn coding by building | Codebitda',
'본문 바로가기':'Skip to content','코드빚다':'Codebitda','소개':'Overview','공개 문제은행':'Problem bank (Korean)','지원':'Support (Korean)','개인정보처리방침':'Privacy policy (Korean)','이용약관':'Terms (Korean)','다른 앱':'Other apps','전체 앱':'All apps (Korean)',
'코드빚다 by Codepretender':'Codebitda by Codepretender','직접 만들며':'Learn to code','배우는 코딩.':'by building.',
'코드를 작성하고 실행하며, 나만의 답을 완성하는 경험.':'Write code, run it, and develop your own solutions.',
'실습부터 과제와 시험까지 하나의 흐름으로 이어갑니다.':'Practice, assignments, and exams in one place.',
'세 프로그램 살펴보기 ↓':'Explore the three apps ↓','공개 문제은행 →':'Problem bank (Korean) →','이용 안내':'Help (Korean)',
'포인터부터 클래스까지.':'From pointers to classes.','코드를 실행하며 동작을 이해합니다.':'Run your code and understand how it works.',
'기능과 앱 화면 살펴보기 →':'Explore features and screenshots →','문법에서 객체지향까지.':'From syntax to object-oriented programming.',
'문제를 풀며 프로그램을 완성합니다.':'Solve problems and build complete programs.',
'텐서 연산부터 회귀와 그래프까지.':'From tensor operations to regression and charts.',
'결과를 보며 데이터의 원리를 익힙니다.':'Explore results and learn how data works.',
'← 코드빚다 전체 앱':'← All Codebitda apps','직접 실행하며':'Learn by running','배우는 C++.':'C++ code.','배우는 Java.':'Java code.','배우는 AI.':'AI code.',
'실습·과제·시험을 한곳에서 시작하세요.':'Start practice, assignments, and exams in one place.',
'macOS 13 이상 · Apple Silicon(M1 이후) 전용 · Intel Mac 미지원':'macOS 13 or later · Apple Silicon (M1 or later) only · Intel Macs are not supported',
'앱의 환경설정 안내에 따라 C++ 실행 도구를 준비합니다.':'Follow the setup guide in the app to prepare the C++ tools.',
'설치 및 보안 경고 안내 →':'Installation and security warnings →',
'임시 서명 · Apple 공증 미적용. 설치 안내문은 DMG 안에도 포함되어 있습니다.':'Ad-hoc signed; not notarized by Apple. The DMG also includes installation instructions in Korean.',
'전체 Xcode 앱은 필요하지 않습니다. C++ 컴파일에는 Apple Command Line Tools를 사용하며, 이미 준비된 Mac은 설치 단계를 건너뜁니다.':'The full Xcode app is not required. C++ compilation uses Apple Command Line Tools. If the tools are already available, you can skip installing them.',
'학생은 Google 로그인 없이 과제·시험에 참여합니다. 교수·조교·마스터는 앱에서 Google 로그인을 사용합니다.':'Students can take assignments and exams without signing in to Google. Instructors, teaching assistants, and the master administrator use Google sign-in in the app.',
'첫 실행 시 보안 경고가 표시될 수 있습니다.':'A security warning may appear the first time you open the app.',
'개발자를 확인할 수 없거나 Apple에서 확인할 수 없다고 나와요.':'macOS says the developer cannot be verified or Apple cannot verify this app.',
'시스템 설정 → 개인정보 보호 및 보안 → 그래도 열기':'System Settings → Privacy & Security → Open Anyway',
'Apple의 Mac 앱 열기 안내 ↗':"Apple’s guide to opening Mac apps ↗",
'앱이 손상되었다는 메시지가 나와요.':'macOS says the app is damaged.',
'이 앱의 설치 안내문 TXT ↓':'Download instructions for this app (TXT) ↓','지원 및 문의 →':'Support and contact (Korean) →',
'직접 풀고,':'Solve problems.','실행하며 확인하세요.':'Run your code and check the results.',
'제공된 문제와 시작 코드를 바탕으로 핵심 코드를 작성합니다. 출력 비교가 가능한 문제는 실행 결과를 확인하고, 수동 채점 문제는 교수자의 검토를 받습니다.':'Write the core code using the provided problems and starter code. Check output for automatically graded problems; instructors review problems that require manual grading.',
'제공된 문제와 시작 코드를 바탕으로 핵심 코드를 작성합니다. 출력 비교가 가능한 문제는 실행 결과를 확인하고, 서술형과 그래프는 교수자의 검토를 받습니다.':'Write the core code using the provided problems and starter code. Check output for automatically graded problems; instructors review written answers and charts.',
'수업의 기록은':'Keep course records','교수자의 Drive에.':"in the instructor’s Drive.",
'교수자는 Google 계정으로 가입하고 승인 후 자신의 Drive를 연결합니다. 초대한 조교와 문제를 수정하고 채점하며, 학생은 Google 로그인 없이 답안을 제출합니다. 제출 파일과 제출학생명단은 연결된 교수자의 폴더에 저장됩니다.':'Instructors register with a Google account and connect their Drive after approval. They can invite teaching assistants to edit problems and grade work. Students submit answers without Google sign-in. Submissions and student submission lists are saved in the connected instructor folder.',
'시험 모드에서는 창 이동 제한과 보조 모니터 가림이 적용됩니다. 과제 모드와 구분해 이용하세요.':'Exam mode restricts switching windows and covers secondary displays. Assignment mode is separate.',
'개인정보처리방침 초안':'Draft privacy policy (Korean)','이용약관 초안':'Draft terms (Korean)','지원 및 문의':'Support and contact (Korean)',
'실제 앱 화면':'App screenshots','과제와 시험을 시작하고, 교수자 홈에서 출제·수정·채점을 관리합니다. 아래 화면은 예시 계정과 테스트 폴더로 촬영했습니다.':'Start assignments and exams, and manage problem creation, editing, and grading from the instructor home. These Korean-language screenshots use example accounts and test folders.',
'과제·시험 시작 화면':'Assignment and exam start screen','교수자 홈':'Instructor home','Google Drive 폴더 관리':'Google Drive folder management',
'콘솔부터 Swing까지.':'From console programs to Swing.',
'Java 실행 환경이 포함되어 있어 별도 JDK 설치가 필요하지 않습니다.':'The Java runtime is included. No separate JDK installation is needed.',
'JDK가 앱에 포함되어 있습니다. Java나 JDK를 따로 설치하거나 경로를 설정할 필요가 없습니다.':'The JDK is included in the app. You do not need to install Java or a JDK separately, or configure paths.',
'Python·TensorFlow 실행 환경이 포함되어 있습니다.':'The Python and TensorFlow runtime is included.',
'Python 3.11·TensorFlow·NumPy·Matplotlib이 앱에 포함되어 있습니다. Python이나 Anaconda를 별도로 설치할 필요가 없습니다.':'Python 3.11, TensorFlow, NumPy, and Matplotlib are included in the app. You do not need to install Python or Anaconda separately.',
'Python·TensorFlow가 포함되어 있습니다.':'Python and TensorFlow are included.',
'별도 설치 없이 Python 3.11, TensorFlow 2.15.1, NumPy, Matplotlib로 실습합니다. Windows CPU 환경을 사용하며, 첫 실행은 라이브러리 준비에 시간이 걸릴 수 있습니다. 실행 속도는 컴퓨터 사양에 따라 달라집니다.':'Practice with Python 3.11, TensorFlow 2.15.1, NumPy, and Matplotlib without separate installations. The Windows version runs on the CPU. Preparing libraries for the first run may take time, and performance depends on your computer.',
'TensorFlow는 Apache License 2.0으로 제공됩니다. Python 및 관련 라이브러리는 각각의 라이선스를 따르며, 배포 앱에 원문 고지가 포함되어 있습니다. 코드빚다는 Google 또는 TensorFlow 프로젝트의 공식 제품이 아닙니다.':'TensorFlow is provided under the Apache License 2.0. Python and other libraries have their own licenses, with original notices included in the app. Codebitda is not an official product of Google or the TensorFlow project.',
'GCC 내장 · C++ 콘솔 실행 · 출력 비교 자동채점 · 교수자 확인 채점 · 20초 간격 암호화 백업 · 교수자 승인 복구를 지원합니다.':'Includes GCC, C++ console execution, output-based automatic grading, instructor grading, encrypted backups every 20 seconds, and instructor-approved recovery.',
'JDK 내장 · 콘솔 및 Swing 실행 · 출력 비교 자동채점 · 교수자 확인 채점 · 20초 간격 암호화 백업 · 교수자 승인 복구를 지원합니다.':'Includes a JDK, console and Swing execution, output-based automatic grading, instructor grading, encrypted backups every 20 seconds, and instructor-approved recovery.',
'Python·TensorFlow CPU 실행 환경 내장 · 코드 실행과 그래프 생성 · 출력 비교 자동채점 · 교수자 확인 채점 · 20초 간격 암호화 백업 · 교수자 승인 복구를 지원합니다.':'Includes a Python and TensorFlow CPU runtime, code execution and charts, output-based automatic grading, instructor grading, encrypted backups every 20 seconds, and instructor-approved recovery.',
'주 메뉴':'Main navigation','코드빚다 프로그램':'Codebitda apps','출제 수정 채점 설정을 선택하는 교수자 홈':'Instructor home with problem creation, editing, grading, and settings','Google Drive 폴더 선택 설정 화면':'Google Drive folder selection settings',
}
APPS=[('cpp','C++','코드빚다-C++','CPP'),('java','Java','코드빚다-JAVA','JAVA'),('ai','AI','코드빚다-AI','AI')]
for slug,title,name,label in APPS:
 D.update({f'코드빚다 : {title}':f'Codebitda: {title}',name:f'Codebitda {title}',f'{title} 2.0.0 | {name}':f'{title} 2.0.0 | Codebitda {title}',f'{label if slug=="java" else title} 2.0.0 · Mac 다운로드 / Windows 심사 중':f'{title} 2.0.0 · Mac available / Windows under review',f'Mac에서 코드빚다 {title}{"을" if slug=="cpp" else "를"} 시작하세요.':f'Get started with Codebitda {title} on Mac.',f'코드빚다 {title} Mac 설치 방법':f'How to install Codebitda {title} on Mac',f'{title} Mac 다운로드로 돌아가기 ↑':f'Back to {title} Mac download ↑',f'코드빚다 {title} 앱 아이콘':f'Codebitda {title} app icon',f'{title} 앱 화면':f'{title} app screenshots',f'과제 시작과 시험 응시를 선택하는 {title} 메인 화면':f'{title} home screen with assignment and exam options',f'현재 Mac 2.0.0은 임시 서명 배포본이며 Apple 공증은 포함되지 않습니다. 이 홈페이지에서 받은 {name} 앱인지 확인하고 아래 안내를 따라 주세요.':f'Mac 2.0.0 is ad-hoc signed and is not notarized by Apple. Make sure you downloaded {name} from this website, then follow the instructions below.',f'다운로드와 앱 복사가 끝났는지 확인하고, 위의 {title} Mac DMG를 다시 다운로드하여 설치해 주세요. 그래도 같은 메시지가 나오면 오류 화면과 macOS 버전을 담당 교강사에게 전달해 주세요.':f'Make sure the download and app copy are complete. Download the {title} Mac DMG above again and reinstall. If the message persists, send a screenshot of the error and your macOS version to your instructor.'})
 D[f'Windows용 {name} 2.0.0'+('을 준비했습니다.' if slug=='java' else '이 심사 중입니다.')]=f'Codebitda {title} 2.0.0 for Windows is under review.'
 D[f'Mac DMG 다운로드 · {dict(cpp=160,java=345,ai=569)[slug]} MB ↓']=f'Download Mac DMG · {dict(cpp=160,java=345,ai=569)[slug]} MB ↓'
D['Windows용 C++ 실습·과제·시험 앱입니다. Microsoft Store 인증 심사에 제출했습니다. 아직 스토어에서 다운로드할 수 없으며, 공개 후 안내합니다. 교수자 서비스는 C++ 앱에서 별도 승인이 필요합니다. Java·AI 앱의 승인은 C++에 자동 적용되지 않습니다.']='The Windows app for C++ practice, assignments, and exams has been submitted for Microsoft Store certification. It is not yet available in the Store; we will announce its release here. Instructor access requires separate approval for C++; Java or AI approval does not automatically apply.'
D['Windows용 Java 실습·과제·시험 앱입니다. Microsoft Store에 제출하여 인증 심사를 진행 중입니다. 아직 스토어에서 다운로드할 수 없으며, 공개 후 안내합니다. 교수자 서비스는 가입 후 승인이 필요합니다.']='The Windows app for Java practice, assignments, and exams is under Microsoft Store certification review. It is not yet available in the Store; we will announce its release here. Instructor access requires approval after registration.'
D['Windows용 AI 실습·과제·시험 앱입니다. Microsoft Store 인증 심사를 요청했습니다. 아직 스토어에서 다운로드할 수 없으며, 공개 후 안내합니다. 교수자 서비스는 AI 앱에서 별도 승인이 필요합니다. Java·C++ 앱의 승인은 AI에 자동 적용되지 않습니다.']='The Windows app for AI practice, assignments, and exams is under Microsoft Store certification review. It is not yet available in the Store; we will announce its release here. Instructor access requires separate approval for AI; Java or C++ approval does not automatically apply.'
FILES=['codebitda.html']+[f'codebitda-{a[0]}.html' for a in APPS]
def english_name(file):return file.replace('.html','-en.html')
def controls(file,en=False):
 return '<div class="language-switch" aria-label="'+('Language' if en else '언어 선택')+'"><a lang="ko" hreflang="ko" href="'+file+'"'+('' if en else ' aria-current="page"')+'>한국어</a><a lang="en" hreflang="en" href="'+english_name(file)+'"'+(' aria-current="page"' if en else '')+'>English</a></div>'
class Translate(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.out=[]
 def handle_decl(self,d):self.out.append('<!'+d+'>')
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='html':attrs['lang']='en'
  for key in ['alt','aria-label']:
   if key in attrs:attrs[key]=D.get(attrs[key],attrs[key])
  if 'href' in attrs:
   h=attrs['href'];stem=h.split('#')[0]
   if stem in FILES:attrs['href']=h.replace(stem,english_name(stem),1)
   if h=='https://support.apple.com/ko-kr/102445':attrs['href']='https://support.apple.com/en-us/102445'
  self.out.append('<'+tag+''.join(' '+k+('="'+escape(v,quote=True)+'"' if v is not None else '') for k,v in attrs.items())+'>')
 def handle_endtag(self,t):self.out.append('</'+t+'>')
 def handle_data(self,s):
  stripped=s.strip();translation=D.get(stripped)
  if translation is None and re.search('[가-힣]',stripped):raise ValueError('Missing translation: '+repr(stripped))
  self.out.append(escape(s if translation is None else s.replace(stripped,translation)))
 def handle_comment(self,s):self.out.append('<!--'+s+'-->')
for file in FILES:
 p=ROOT/file;s=p.read_text()
 # Regenerate from the Korean source without duplicating the language control.
 s=re.sub(r'<div class="language-switch".*?</div>','',s)
 s=re.sub(r'<link rel="(?:alternate)"[^>]*>','',s)
 s=s.replace('<link rel="stylesheet" href="codebitda-language.css">','')
 source=s
 source=source.replace('</head>','<link rel="stylesheet" href="codebitda-language.css"><link rel="alternate" hreflang="ko" href="https://codepretender.com/'+file+'"><link rel="alternate" hreflang="en" href="https://codepretender.com/'+english_name(file)+'"></head>')
 p.write_text(source.replace('</nav>',controls(file)+'</nav>',1))
 if file!='codebitda.html':
  slug=file.removeprefix('codebitda-').removesuffix('.html');_,title,name,label=next(x for x in APPS if x[0]==slug)
  if slug=='cpp':steps=[f'Download the C++ Mac DMG above and open it.',f'Open <strong>{name}.app</strong> inside the DMG. If a security warning appears, see the guidance below.','In <strong>코드빚다 C++ 환경설정 (C++ Setup)</strong>, click <strong>설치 시작 (Start installation)</strong> to install the app in Applications.','If the tools are missing, click <strong>Apple 실행 도구 설치 (Install Apple tools)</strong> and complete the Apple installer. An internet connection may be required.','Click <strong>설치 완료 여부 확인 (Check installation)</strong>. After the C++ check passes, click <strong>앱 실행 (Open app)</strong>.',f'From then on, open {name} from Applications. You can eject the installation disk.']
  else:
   steps=[f'Download the {title} Mac DMG above and open it.',f'Drag <strong>{name}.app</strong> to the <strong>Applications</strong> folder inside the DMG.',f'When copying is complete, open <strong>{name}</strong> from Applications in Finder. If a security warning appears, see the guidance below.']
   if slug=='ai':steps+=['The first code run may take a little longer while Python and TensorFlow initialize. Please wait.']
   steps+=['Once the app opens, select the assignment or exam option as instructed by your instructor. You can eject the installation disk.']
  # Protect complete English instructions and literal Korean labels from word-level translation.
  s=re.sub(r'<ol>.*?</ol>','<ol>INSTALL_STEPS_PLACEHOLDER</ol>',s,count=1)
  pattern=r'<p>'+re.escape(name)+r' 실행을 한 번 시도한 뒤.*?</p>'
  s=re.sub(pattern,'<p>SECURITY_STEPS_PLACEHOLDER</p>',s,count=1)
  s=s.replace(f'codebitda-{slug}-mac-install.txt',f'codebitda-{slug}-mac-install-en.txt')
 t=Translate();t.feed(s);en=''.join(t.out)
 if file!='codebitda.html':
  security=f'Try opening {name} once, then check <strong>System Settings → Privacy &amp; Security → Open Anyway</strong>. Make sure the app name matches {name}. On a school-managed Mac, contact your administrator if you cannot allow it.'
  en=en.replace('INSTALL_STEPS_PLACEHOLDER',''.join('<li>'+x+'</li>' for x in steps)).replace('SECURITY_STEPS_PLACEHOLDER',security)
  en=en.replace('<ol>','<p>These instructions are in English. App buttons may still appear in Korean; the original labels are shown below where needed.</p><ol>',1)
  txt=[f'Codebitda {title} 2.0.0 — Mac installation','macOS 13 or later. Apple Silicon (M1 or later) only. Intel Macs are not supported.','']+[f'{i}. '+re.sub('<[^>]+>','',x) for i,x in enumerate(steps,1)]+['','Security warnings','This version is ad-hoc signed and is not notarized by Apple.',re.sub('<[^>]+>','',security).replace('&amp;','&'),'If the app is reported as damaged, download and reinstall it from this website. If the message persists, send the error and your macOS version to your instructor.','','Full guide: https://codepretender.com/'+english_name(file)+'#mac-install']
  (ROOT/f'codebitda-{slug}-mac-install-en.txt').write_text('\n'.join(txt)+'\n')
 en=en.replace('https://codepretender.com/'+file,'https://codepretender.com/'+english_name(file))
 en=en.replace('</head>','<link rel="stylesheet" href="codebitda-language.css"><link rel="alternate" hreflang="ko" href="https://codepretender.com/'+file+'"><link rel="alternate" hreflang="en" href="https://codepretender.com/'+english_name(file)+'"></head>')
 en=en.replace('</nav>',controls(file,True)+'</nav>',1)
 (ROOT/english_name(file)).write_text(en)

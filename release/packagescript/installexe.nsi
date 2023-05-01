; �ýű�ʹ�� HM VNISEdit �ű��༭���򵼲���

; ��װ�����ʼ���峣��
!define PRODUCT_NAME "��ѧʽ���㹤��"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "Html5syt."
!define PRODUCT_WEB_SITE "https://github.com/html5syt/Chemical-formula-calculation-tool/tree/%E5%8F%82%E8%B5%9B%E7%89%88%E6%9C%AC"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\main.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

SetCompressor lzma

; ------ MUI �ִ����涨�� (1.67 �汾���ϼ���) ------
!include "MUI.nsh"

; MUI Ԥ���峣��
!define MUI_ABORTWARNING
!define MUI_ICON "..\source\icon.ico"
!define MUI_UNICON "..\source\uninstall.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\source\left.bmp"

; ��ӭҳ��
!insertmacro MUI_PAGE_WELCOME
; ���Э��ҳ��
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "..\source\licence.txt"
; ��װĿ¼ѡ��ҳ��
!insertmacro MUI_PAGE_DIRECTORY
; ��ʼ�˵�����ҳ��
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "��ѧʽ���㹤��-������"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; ��װ����ҳ��
!insertmacro MUI_PAGE_INSTFILES
; ��װ���ҳ��
!define MUI_FINISHPAGE_RUN "$INSTDIR\main.exe"
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\Help.mhtml"
!insertmacro MUI_PAGE_FINISH

; ��װж�ع���ҳ��
!insertmacro MUI_UNPAGE_INSTFILES

; ��װ�����������������
!insertmacro MUI_LANGUAGE "SimpChinese"

; ��װԤ�ͷ��ļ�
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI �ִ����涨����� ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "CFCT-Install.exe"
InstallDir "$PROGRAMFILES\Chemical-formula-calculation-tool"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "��ѧʽ���㹤�� V1.0-������"

Section "��ѧʽ���㹤��" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File "..\source\about.jpg"
  File "..\source\font.ttf"
  File "..\source\function.py"
  File "..\source\Help.mhtml"
  File "..\source\icon.ico"
  File "..\source\licence.txt"
  File "..\source\main.exe"
  File "..\source\main.py"
  File "..\source\PTOElist.py"
  File "..\source\window.py"

; ������ʼ�˵���ݷ�ʽ
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\��ѧʽ���㹤��.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$DESKTOP\��ѧʽ���㹤��.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\���߰�����ļ�.lnk" "$INSTDIR\Help.mhtml"
  CreateShortCut "$STARTMENU\��ѧʽ���㹤��.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$DESKTOP\���߰�����ļ�.lnk" "$INSTDIR\Help.mhtml"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -AdditionalIcons
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\main.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\main.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  �����ǰ�װ�����ж�ز���  *
 ******************************/

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\window.py"
  Delete "$INSTDIR\PTOElist.py"
  Delete "$INSTDIR\main.py"
  Delete "$INSTDIR\main.exe"
  Delete "$INSTDIR\licence.txt"
  Delete "$INSTDIR\icon.ico"
  Delete "$INSTDIR\Help.mhtml"
  Delete "$INSTDIR\function.py"
  Delete "$INSTDIR\font.ttf"
  Delete "$INSTDIR\about.jpg"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\���߰�����ļ�.lnk"
  Delete "$STARTMENU\��ѧʽ���㹤��.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\���߰�����ļ�.lnk"
  Delete "$DESKTOP\��ѧʽ���㹤��.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\��ѧʽ���㹤��.lnk"

  RMDir "$SMPROGRAMS\$ICONS_GROUP"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- ���� NSIS �ű��༭�������� Function ���α�������� Section ����֮���д���Ա��ⰲװ�������δ��Ԥ֪�����⡣--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "��ȷʵҪж�ػ�ѧʽ���㹤��-�����棿���ٿ���һ����(�� �㧥 ��;)��" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "����ѧʽ���㹤�ߡ���ж�ء�"
FunctionEnd

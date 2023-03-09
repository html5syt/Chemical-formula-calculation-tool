; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "化学式计算工具"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "Html5syt."
!define PRODUCT_WEB_SITE "https://github.com/html5syt/Chemical-formula-calculation-tool/tree/%E5%8F%82%E8%B5%9B%E7%89%88%E6%9C%AC"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\main.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

SetCompressor lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "..\source\icon.ico"
!define MUI_UNICON "..\source\uninstall.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\source\left.bmp"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "..\source\licence.txt"
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 开始菜单设置页面
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "化学式计算工具-参赛版"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$INSTDIR\main.exe"
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\Help.mhtml"
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "CFCT-Install.exe"
InstallDir "$PROGRAMFILES\Chemical-formula-calculation-tool"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "化学式计算工具 V1.0-参赛版"

Section "化学式计算工具" SEC01
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

; 创建开始菜单快捷方式
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\化学式计算工具.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$DESKTOP\化学式计算工具.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\离线版帮助文件.lnk" "$INSTDIR\Help.mhtml"
  CreateShortCut "$STARTMENU\化学式计算工具.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$DESKTOP\离线版帮助文件.lnk" "$INSTDIR\Help.mhtml"
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
 *  以下是安装程序的卸载部分  *
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
  Delete "$DESKTOP\离线版帮助文件.lnk"
  Delete "$STARTMENU\化学式计算工具.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\离线版帮助文件.lnk"
  Delete "$DESKTOP\化学式计算工具.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\化学式计算工具.lnk"

  RMDir "$SMPROGRAMS\$ICONS_GROUP"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要卸载化学式计算工具-参赛版？不再考虑一下吗(っ °Д °;)っ" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "【化学式计算工具】已卸载。"
FunctionEnd

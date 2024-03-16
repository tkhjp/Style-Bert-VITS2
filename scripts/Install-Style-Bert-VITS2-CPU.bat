chcp 65001 > NUL
@echo off

@REM https://github.com/Zuntan03/EasyBertVits2 より引用・改変

pushd %~dp0
set PS_CMD=PowerShell -Version 5.1 -ExecutionPolicy Bypass

set CURL_CMD=C:\Windows\System32\curl.exe
if not exist %CURL_CMD% (
	echo [ERROR] %CURL_CMD% が見つかりません。
	pause & popd & exit /b 1
)

@REM lib フォルダがなければ作成
if not exist lib\ ( mkdir lib )

@REM Style-Bert-VITS2.zip をGitHubのmasterの最新のものをダウンロード
%CURL_CMD% -Lo Style-Bert-VITS2.zip^
	https://github.com/litagin02/Style-Bert-VITS2/archive/refs/heads/master.zip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM Style-Bert-VITS2.zip を解凍（フォルダ名前がBert-VITS2-masterになる）
%PS_CMD% Expand-Archive -Path Style-Bert-VITS2.zip -DestinationPath . -Force
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM 元のzipを削除
del Style-Bert-VITS2.zip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM Bert-VITS2-masterの中身をStyle-Bert-VITS2に上書き移動
xcopy /QSY .\Style-Bert-VITS2-master\ .\Style-Bert-VITS2\
rmdir /s /q Style-Bert-VITS2-master

echo ----------------------------------------
echo Setup Python and Virtual Environment
echo ----------------------------------------

@REM Pythonと仮想環境のセットアップを呼び出す（仮想環境が有効化されて戻ってくる）
call Style-Bert-VITS2\scripts\Setup-Python.bat ..\..\lib\python ..\venv
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

@REM 依存関係インストール
pip install -r Style-Bert-VITS2\requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

echo ----------------------------------------
echo Environment setup is complete. Start downloading the model.
echo ----------------------------------------

@REM Style-Bert-VITS2フォルダに移動
pushd Style-Bert-VITS2

@REM 初期化（必要なモデルのダウンロード）
python initialize.py

echo ----------------------------------------
echo Model download is complete. Start Style-Bert-VITS2 Editor.
echo ----------------------------------------

@REM エディターの起動
python server_editor.py --inbrowser

pause

popd

popd


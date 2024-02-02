pyinstaller main.py --workpath build --distpath output ^
	-n word --add-data "bgm.mp3;." --add-data "content.png;." ^
	--add-data "window.png;." -i "app.ico" --version-file "version_info.txt" ^
	--onefile --clean --noconsole --noconfirm
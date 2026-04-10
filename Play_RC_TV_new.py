import os
import subprocess 
import time 
import schedule 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
 
WATCHED_DIR = r'\\dalimo.ru\userdocsSPB\Корпоративные материалы\Медиафайлы' #Директория с видео  
PLAYLIST_DIR = r'C:\Playlist' #Директория, где будет создан плейлист 
PLAYLIST_FILE = os.path.join(PLAYLIST_DIR, 'playlist.m3u') 
VLC_PATH = r"C:\Program Files\VideoLAN\VLC\vlc.exe" 
DEBOUNCE_INTERVAL = 1  
 
vlc_process = None 
 
def update_playlist(): 
    if not os.path.exists(PLAYLIST_DIR): 
        os.makedirs(PLAYLIST_DIR) 
 
    media_files = sorted([f for f in os.listdir(WATCHED_DIR) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]) 
     
    with open(PLAYLIST_FILE, 'w', encoding='utf-8') as f: 
        for file in media_files: 
            f.write(os.path.join(WATCHED_DIR, file) + '\n') 
     
    print("Плейлист обновлен.") 
 
def start_vlc(): 
    global vlc_process 
    try: 
        print("Запуск VLC...") 
        vlc_process = subprocess.Popen([ 
            VLC_PATH, 
            "--fullscreen", 
            "--no-video-title-show", 
            "--loop",
            "--no-qt-privacy-ask",             # Без диалога конфиденциальности
            "--no-qt-error-dialogs",           # Без ошибок на экране
            "--no-qt-updates-notif",           # Без уведомлений об обновлениях
            "--no-qt-system-tray",             # Без иконки в трее
            "--no-qt-name-in-title",           # Без надписи VLC в заголовке
            PLAYLIST_FILE
        ]) 
        print("VLC запущен.") 
    except Exception as e: 
        print(f"Ошибка при запуске VLC: {e}") 
 
def stop_vlc(): 
    global vlc_process 
    if vlc_process: 
        print("Остановка VLC...") 
        vlc_process.terminate() 
        vlc_process.wait() 
        vlc_process = None 
        print("VLC остановлен.") 
 
def scheduled_task(): 
    print("Выполнение запланированной задачи...") 
    update_playlist() 
    stop_vlc() 
    start_vlc() 
 
def run_scheduler(): 
 
    schedule.every().day.at("20:00").do(scheduled_task) 
 
    while True: 
        schedule.run_pending() 
        time.sleep(5) 
 
if __name__ == "__main__": 
 
    scheduled_task() 
     
    run_scheduler()
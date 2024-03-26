import shutil
import os
from datetime import datetime

def create_backup(source_file, backup_dir):
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Get current date
    now = datetime.now()
    date_folder = now.strftime("%Y.%m.%d")

    # Path to the backup folder
    backup_path = os.path.join(backup_dir, date_folder)

    # Create date folder if it doesn't exist
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    # Copy the file to the backup folder
    shutil.copy(source_file, backup_path)

if __name__ == "__main__":
    source_file_path = r"C:\Users\luca.girardi\SUGOI CONSTRUTORA S.A\Financeiro - Contas a Pagar\04 - FIDCS\ACOMPANHAMENTO FIDC.xlsx"
    backup_directory = r"C:\Users\luca.girardi\SUGOI CONSTRUTORA S.A\Financeiro - Contas a Pagar\04 - FIDCS\BACKUP SEMANAL FIDC"
    
    create_backup(source_file_path, backup_directory)

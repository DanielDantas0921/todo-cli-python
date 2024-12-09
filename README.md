para executar o projeto acesse o caminho da pasta e rode o comando python task_tracker.py (comando) (subcomandos ou argumentos)
exemplos

python task_tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python task_tracker.py update 1 "Buy groceries and cook dinner"
python task_tracker.py delete 1

# Marking a task as in progress or done
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1

# Listing all tasks
python task_tracker.py list

# Listing tasks by status
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress

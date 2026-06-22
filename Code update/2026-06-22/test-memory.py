
from memory import add_message,load_history

test_file = "test_memory.json"
add_message("user", "你好", file_path=test_file)
add_message("assistant", "你好啊", file_path=test_file)
history = load_history(test_file)
print(history)
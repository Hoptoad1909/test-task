import importlib


scripts = {
    'script1': 'script1_module',
    'script2': 'script2_module',
    'script3': 'script3_module',
    'script4': 'script4_module',
    'script5': 'script5_module'
}


while True:
    print("Available scripts:")
    for key in scripts:
        print(key)

    user_input = input("Enter the script name to run (or 'exit' to complete): ")

    if user_input.lower() == 'exit':
        break

    if user_input in scripts:
        try:
            module = importlib.import_module(scripts[user_input])
            module.run()
        except ImportError:
            print("error: script not found")
    else:
        print("error: script not found")
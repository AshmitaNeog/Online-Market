from market import app

# checks if run.py executes directly and not by importing
if __name__ == '__main__':
    app.run(debug=True)

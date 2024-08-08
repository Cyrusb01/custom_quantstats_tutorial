# How to Use Custom Tearsheet with Quantstats

## Installation

1. **Install the Custom Quantstats Package**:
   ```bash
   python -m pip install -e git+https://github.com/bfcdev/quantstats@custom_tearsheet#egg=QuantStats
   ```
2. **Import the Package**:
    ```python 
    import quantstats as qs
    ```
3. **Explore Customizations**:  
Check out the `example.py` file to see all the new customaizations you 

## Development Process

### Initial Setup
1. Fork the main Quantstats repository.
2. Create a new branch named `custom_tearsheet`.
3. Clone the repository to your local machine.

### Making Customizations
1. Edit the `html` function and supporting graphing functions as needed.
2. Push the changes to your branch.

### Installation Note
Quantstats is a PyPi package with a `setup.py` file, making the installation of the edited package straightforward with the command provided above.

## Additional Thoughts

### Dependency Management
Since this fork was created some time ago, some dependencies might deprecate certain functions. To avoid issues, it's best to use the `requirements.txt` file and install the packages with the same versions. This project is compatible with Python 3.12.4.

### Handling Deprecation Issues
For example, I encountered an issue where `np.product` was deprecated. Here’s how I fixed it:
1. The installation command above creates a local, editable version of the package with a `src/quantstats` directory.
2. Locate where `np.product` is used, navigate to `src/quantstats/quantstats/stats.py`, make the necessary edit, and test it.
3. To make the change permanent:
    - Clone the repository from here.
    - Navigate to the `custom_tearsheet` branch.
    - Make the edits and push them to GitHub.

### Quick Changes
If you need to omit plots from the tearsheet:
1. Navigate to `src/quantstats/quantstats/report.html`.
2. Edit lines 34-46 to remove the unwanted graphs.





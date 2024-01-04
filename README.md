# Replication Package for "Rubber Duckies and Fishes"
This project aims to reproduce a chapter of a textbook, regarding the sales of rubber duckies and fishes.

## Building the Docker image

- Clone the repository
    
    ```bash
    git clone https://github.com/maojcn/project_duckies.git
    ```

- Build the Docker image

    ```bash
    cd project_duckies
    docker build -t duckies .
    ```

<<<<<<< HEAD
    > docker build -t duckies .

- Run the Docker container

    >docker run duckies
=======
- Run the Docker container

    ```bash
    docker run duckies
    ```
- To copy files from a Docker container to the host machine
    - Find the container ID or name:
        ```bash
        docker ps
        ```
    - Copy files from the container to the host:
        ```bash
        docker cp <container_id_or_name>:<container_path> <host_path>
        ```

## Results

- Figures:

    path: `report/figures`
    - feasible_region.png
    - historical_sales.png

- Results of Optimization:

    path: `results/`
    - optimized_results.csv

- Report:

    path: `report/`
    - main.pdf

## Sources

* [Bathing friends unlimited](https://resources.oreilly.com/examples/9780596153946/-/blob/master/bathing_friends_unlimited.xls)
* [Historical sales data](https://resources.oreilly.com/examples/9780596153946/-/blob/master/historical_sales_data.xls)
* [Micheal Milton, Head First Data Analysis, 75-109](https://www.oreilly.com/library/view/head-first-data/9780596806224/)

## License
This project is licensed under the MIT License.

## Acknowledgments

This project makes use of the following open-source tools and libraries:

- [Matplotlib](https://matplotlib.org/) - A 2D plotting library for Python.
  - Used for creating visualizations and plots.

- [NumPy](https://numpy.org/) - The fundamental package for scientific computing with Python.
  - Utilized for efficient numerical operations and array manipulations.

- [PuLP](https://coin-or.github.io/pulp/) - A linear programming optimization library.
  - Employed for solving linear programming problems in optimization scenarios.

- [Pandas](https://pandas.pydata.org/) - A powerful data manipulation and analysis library.
  - Used for handling and analyzing structured data.

- [LaTeXmk](https://mg.readthedocs.io/latexmk.html) - A Perl script for automating the process of running LaTeX to produce a document.
  - Streamlines the document compilation workflow.

- [Perl](https://www.perl.org/) - A high-level, general-purpose programming language.
  - Used by LaTeXmk for scripting and automation.

- [TeX Live](https://www.tug.org/texlive/) - A comprehensive TeX distribution that includes a wide range of TeX-related programs and packages.
  - Provides the TeX typesetting system used in this project.
>>>>>>> 1729334 (Add MIT License to the project)

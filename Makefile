historical_sales.png: scripts/plotting_history.py
	python3 scripts/plotting_history.py

feasible_region.png: scripts/plotting_constrains.py
	python3 scripts/plotting_constrains.py

main.pdf: feasible_region.png historical_sales.png
	cd report && latexmk -pdf -silent main.tex && latexmk -c && cd ..
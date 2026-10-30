# Aryabhatiya Computational Algorithms (Streamlit app)

Step-by-step Python implementations of three algorithms from Aryabhata's
*Aryabhatiya* (499 CE): **Kuttaka** (modular inverse), **square-root**
extraction (Varga) and **cube-root** extraction (Ghana). The program follows
the ancient steps and then double-checks each answer with a modern function.

## Files
| File | Purpose |
|---|---|
| `streamlit_app.py` | The web app (choose an algorithm, enter numbers, see the steps) |
| `ancient_algorithms.py` | The ancient-method code (returns result + full step trace) |
| `modern_checks.py` | Modern functions used ONLY to verify the answers |
| `cli.py` | Optional terminal version |
| `verify.py` | Worked examples + 1000 random tests per algorithm |
| `requirements.txt` | Needs only `streamlit` |

## Run on your computer
```
pip install -r requirements.txt
streamlit run streamlit_app.py
```
It opens at http://localhost:8501

## Put it on GitHub and make it live (free)
1. Create a new **public** repository on github.com.
2. Upload ALL files from this folder (keep `.streamlit/config.toml`).
3. Go to https://share.streamlit.io, sign in with GitHub, click **New app**.
4. Pick your repository, branch `main`, main file `streamlit_app.py`, click **Deploy**.
5. After a minute you get a public link such as `https://your-app.streamlit.app`.

## Terminal version (no Streamlit needed)
```
python cli.py
python verify.py
```

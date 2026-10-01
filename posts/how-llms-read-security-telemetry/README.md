# How LLMs Read Security Telemetry

The notebook behind
[Understanding How LLMs Process Security Telemetry](https://henryparks.com/research/how-llms-read-security-telemetry/).
It reruns the post's measurements in the same order as its sections. The one exception is the private
Sysmon export behind Figure 8, which you can replace with your own.

## Run it

Open it in Google Colab with the badge at the top of the notebook, or run it locally from the top of your
clone:

```bash
cd research-notebooks
python -m venv .venv
.venv\Scripts\activate            # on macOS or Linux: source .venv/bin/activate
pip install -r posts/how-llms-read-security-telemetry/requirements.txt
jupyter notebook posts/how-llms-read-security-telemetry/how-llms-read-security-telemetry.ipynb
```

Create the environment at the top of your clone, as above. On Windows, a deeper folder can push some
installed file paths past the 260-character limit, and `pip install` then fails with an `OSError` about a
missing file.

Sections 7 and 8 load the full model and need a GPU with 16 GB of memory. Without one, their cells print a
note and are skipped, so Run All still finishes. Everything else runs on a
laptop with about 3 GB of free memory, after a one-time 4.9 GB download. On Windows, pip installs the
CPU build of PyTorch. For a GPU, install `torch==2.14.0` from
[pytorch.org](https://pytorch.org/get-started/locally/) first.

## Run it on your own telemetry

Export Sysmon event ID 1 to an `.evtx` file and set `EVTX_PATH` in the notebook's last section. It
prints totals only, and nothing from your events is saved.

## Antivirus

The data file and the notebook contain real attack command lines, so endpoint protection may flag them.
See [data/README.md](data/README.md).

## License

MIT for the code and notebook. The data comes from Atomic Red Team (MIT, copyright Red Canary).

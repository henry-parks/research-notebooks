# Research notebooks

Rerun the measurements from the security research on [henryparks.com](https://henryparks.com/research/).
Each notebook follows its post section by section and is written for SOC analysts and detection
engineers.

<!-- index:start -->
<!-- Generated from each post's post.toml. Do not edit this table by hand. -->
| Post | Published | Run it | Needs a GPU? |
| --- | --- | --- | --- |
| Understanding How LLMs Process Security Telemetry | not yet | [folder](posts/how-llms-read-security-telemetry/) | Sections 7 and 8 only |
<!-- index:end -->

## Run it locally

```bash
git clone https://github.com/henry-parks/research-notebooks
cd research-notebooks
python -m venv .venv
.venv\Scripts\activate            # on macOS or Linux: source .venv/bin/activate
pip install -r posts/<folder>/requirements.txt
jupyter notebook posts/<folder>
```

Keep the environment at the top of the clone. On Windows, a deeper folder can exceed the 260-character path
limit during install.

For the exact code behind a post, check out the tag the post links to.

## Not in this repository

Private telemetry, standalone tools and exploit code are never published here. Posts built on real
logs share aggregate numbers only.

Code and notebooks are MIT licensed.

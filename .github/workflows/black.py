name: Black

on: push

jobs:
  black:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - name: Install black
        run: |
          python -m pip install --upgrade pip
          python -m pip install black
      - name: Run black
        run: black Music
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v3
        with:
          commit-message: Automated code formatting
          title: Format code.
          body: Automated code formatting.
          labels: ⚫️ black
          branch: autofix
          committer: idzero23<80420642+idzero23@users.noreply.github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          signoff: true
          delete-branch: true

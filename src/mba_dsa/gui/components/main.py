from ..components._base import Label
from ._base import BasePage_


class MainPage(BasePage_):
    title: Label = Label(
        emoji="\U0001f4da",  # 📚
        text="MBA Data Science and Analytics",
    )

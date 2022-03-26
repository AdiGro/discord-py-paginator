from __future__ import annotations

from discord import ButtonStyle, User, Interaction
from discord.ext.commands import Bot

from . import button, errors, modals

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .paginator import Paginator

class FirstElement(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.secondary,
            label="\U000025c0 \U000025c0",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await self.parent.set_page(1)
        await interaction.response.edit_message(
            **await self.parent.get_page_content()
        )


class PreviousElement(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.blurple,
            label="\U000025c0",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await self.parent.set_page(self.parent.page-1)
        await interaction.response.edit_message(
            **await self.parent.get_page_content()
        )



class NextElement(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.blurple,
            label="\U000025b6",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await self.parent.set_page(self.parent.page + 1)
        await interaction.response.edit_message(
            **await self.parent.get_page_content()
        )



class LastElement(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.secondary,
            label="\U000025b6 \U000025b6",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await self.parent.set_page(await self.parent.get_page_count())
        await interaction.response.edit_message(
            **await self.parent.get_page_content()
        )

class Stop(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.danger,
            label="Quit",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        self.parent.stop()
        await interaction.response.send_message(
            content="Stopped",
            ephemeral=True
        )


class Start(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.success,
            label="Start",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await self.parent.started_pressed()
        await self.parent.set_page(1)
        values = await self.parent.get_page_content()
        values.update({"view": self.parent})

        await interaction.response.edit_message(
            **values
        )

class QuickNav(button.BetterButton):
    def __init__(
            self,
            client: Bot,
            parent: Paginator,
            user: User,
            disabled: bool = True
    ):
        super().__init__(
            style=ButtonStyle.blurple,
            label="Nav",
            disabled=disabled
        )
        self.client = client
        self.parent = parent
        self.user = user

    @button.button_check(1)
    async def check_author(self, interaction: Interaction) -> bool:
        if interaction.user != self.user:
            raise errors.NotAuthor("You are not allowed to do this")

        return True

    async def on_error(self, interaction: Interaction, error: errors.ButtonException):
        await interaction.response.send_message(
            content=error.message,
            ephemeral=True
        )

    async def on_click(self, interaction: Interaction):
        await interaction.response.send_modal(modals.QuickNav(parent=self.parent, user=self.user))

class Placeholder(button.BetterButton):
    def __init__(
            self
    ):
        super().__init__(
            style=ButtonStyle.secondary,
            label="\U0001f6ab",
            disabled=True
        )

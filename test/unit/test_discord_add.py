import unittest
from unittest.mock import MagicMock, patch
from discordBot import add  # Replace 'your_module' with the actual module name

class TestAddCommand(unittest.TestCase):

    def setUp(self):
        self.ctx = MagicMock()
        self.ctx.author = "user1"
        self.ctx.channel = "channel1"

    @patch('discordBot.process_date')
    async def test_select_date(self, mock_process_date):
        self.ctx.send.side_effect = ["03-02-2023"]
        await add.select_date(self.ctx)

        self.ctx.send.assert_called_with("Enter day")
        mock_process_date.assert_called_with(self.ctx, 2, 3, 2023)

    @patch('discordBot.bot.wait_for')
    @patch('discordBot.process_date')
    async def test_select_date_timeout(self, mock_process_date, mock_wait_for):
        mock_wait_for.side_effect = asyncio.TimeoutError
        await add.select_date(self.ctx)
        self.ctx.send.assert_called_with("You took too long to respond. Please try again.")

    @patch('discordBot.process_category')
    async def test_process_date(self, mock_process_category):
        await add.process_date(self.ctx, 2, 3, 2023)
        self.ctx.send.assert_called_with("Selected Date: 03-02-2023")
        mock_process_category.assert_called_with(self.ctx, datetime(2023, 3, 2))

    @patch('discordBot.Select')
    @patch('discordBot.View')
    @patch('discordBot.bot.wait_for')
    async def test_select_category(self, mock_wait_for, mock_view, mock_select):
        mock_wait_for.side_effect = ["selected_category"]
        mock_select.return_value.values = ["selected_category"]
        user_list = {"channel1": {"spend_categories": ["category1", "category2"]}}
        self.ctx.author = "user1"
        self.ctx.channel = "channel1"

        await add.select_category(self.ctx, datetime(2023, 3, 2))
        self.ctx.send.assert_called_with('Please select a category')
        self.ctx.send.assert_called_with("You chose: selected_category")

    @patch('discordBot.post_category_selection')
    async def test_select_category_invalid_category(self, mock_post_category_selection):
        await add.select_category(self.ctx, datetime(2023, 3, 2))
        self.ctx.send.assert_called_with('Please select a category')
        self.ctx.send.assert_called_with("Invalid category")

    @patch('discordBot.bot.wait_for')
    @patch('discordBot.post_amount_input')
    async def test_post_category_selection(self, mock_post_amount_input, mock_wait_for):
        mock_wait_for.side_effect = ["50"]
        await add.post_category_selection(self.ctx, "category1", datetime(2023, 3, 2))
        self.ctx.send.assert_called_with('\nHow much did you spend on category1')
        mock_post_amount_input.assert_called_with(self.ctx, "50", "category1", datetime(2023, 3, 2))

    @patch('discordBot.bot.wait_for')
    @patch('discordBot.user_list', {"channel1": {"monthly_budget": 100}})
    async def test_post_category_selection_zero_amount(self):
        await add.post_category_selection(self.ctx, "category1", datetime(2023, 3, 2))
        self.ctx.send.assert_called_with("Spent amount has to be a non-zero number.")

    @patch('discordBot.bot.wait_for')
    @patch('discordBot.user_list', {"channel1": {"monthly_budget": 100}})
    async def test_post_category_selection_valid_amount(self):
        await add.post_category_selection(self.ctx, "category1", datetime(2023, 3, 2))
        self.ctx.send.assert_called_with("The following expenditure has been recorded: You have spent $50 for category1 on 03-02-2023")

if __name__ == '__main__':
    unittest.main()
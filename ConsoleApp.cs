// C#
using System;
using System.Threading.Tasks;
using SlackNet;
using SlackNet.Events;
using SlackNet.SocketMode;

class Program
{
    static async Task Main(string[] args)
    {
        string appToken = "xapp-your-app-token"; // Your app-level token
        string botToken = "xoxb-your-bot-token"; // Your bot token

        var slackSocketModeClient = new SlackSocketModeClient(appToken, botToken);

        slackSocketModeClient.OnEvent<MessageEvent>(async message =>
        {
            if (message.Text.Equals("Hello", StringComparison.OrdinalIgnoreCase))
            {
                await slackSocketModeClient.Chat.PostMessage(new Message
                {
                    Channel = message.Channel,
                    Text = "Hello"
                });
            }
        });

        await slackSocketModeClient.Connect();
        Console.WriteLine("Connected to Slack via Socket Mode. Listening for messages...");

        // Keep the application running
        await Task.Delay(-1);
    }
}

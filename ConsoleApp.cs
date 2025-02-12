// C#
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string botToken = "xoxb-your-bot-token";
        string appToken = "xapp-your-app-token"; // Typically used for Socket Mode, not needed here
        string channelId = "your-channel-id";

        // Listen for messages (this is a placeholder for actual message listening logic)
        string incomingMessage = "Hello"; // Simulated incoming message

        if (incomingMessage.Equals("Hello", StringComparison.OrdinalIgnoreCase))
        {
            await SendMessageToSlack(channelId, "Hello", botToken);
        }
    }

    static async Task SendMessageToSlack(string channelId, string message, string token)
    {
        var payload = new JObject
        {
            { "channel", channelId },
            { "text", message }
        };

        var requestContent = new StringContent(payload.ToString(), Encoding.UTF8, "application/json");
        client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);

        HttpResponseMessage response = await client.PostAsync("https://slack.com/api/chat.postMessage", requestContent);

        if (response.IsSuccessStatusCode)
        {
            Console.WriteLine("Message sent successfully!");
        }
        else
        {
            Console.WriteLine($"Failed to send message. Status code: {response.StatusCode}");
        }
    }
}

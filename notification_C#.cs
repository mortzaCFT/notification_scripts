// This is notification script runs on an console app program.
// For run this you will need to get Notification lib with the nuget package.
// Best way for sending toast notification in the windows 10/11 is using xml for sending notif.
// writed by mortzaCFT.

using System;
using Windows.Data.Xml.Dom;
using Windows.UI.Notifications;

namespace notifi_pip
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string title = "";
            string body = "";
            string image = "";
            string AppId = "";
            //  public const string AppId = "Microsoft.WindowsAlarms_8wekyb3d8bbwe!App";

            for (int i = 0; i < args.Length; i++)
            {
                switch (args[i])
                {
                    case "--title":
                        if (i + 1 < args.Length) title = args[++i];
                        else throw new ArgumentException("Missing value for --title");
                        break;
                    case "--body":
                        if (i + 1 < args.Length) body = args[++i];
                        else throw new ArgumentException("Missing value for --body");
                        break;
                    case "--image":
                        if (i + 1 < args.Length) image = args[++i];
                        break;
                    case "--appname":
                        if (i + 1 < args.Length) AppId = args[++i];
                        else throw new ArgumentException($"Unknown option: {args[i]}");
                        break;
                }
            }

            if (string.IsNullOrEmpty(title))
            {
                title = " ";
            }
            if (string.IsNullOrEmpty(body))
            {
                body = " ";
            }
            if (string.IsNullOrEmpty(AppId))
            {
                AppId = " ";
            }
            // ShowTile(string title, string body, string image, string appId)
            ShowNotification(title, body, image, AppId);
        }

        public static string DetectLanguage(string sentence)
        {
            if ('\u0600' <= sentence[0] && sentence[0] <= '\u06FF')
            {
                return "right";
            }

            else if ('A' <= char.ToUpper(sentence[0]) && char.ToUpper(sentence[0]) <= 'Z')
            {
                return "left";
            }
            else
            {
                return "left";
            }
        }

        public static void ShowNotification(string title, string body, string image, string appId)
        {
            string LangT = DetectLanguage(body);
            string LangB = DetectLanguage(body);

            var toastXml = $@" <toast lang='fa-IR'> <visual> <binding template='ToastGeneric'> 
<image placement='appLogoOverride' hint-crop='circle' src='{image}' />
                            <group>
                              <subgroup>
                               <text   hint-align='{LangT}'>{title}</text>
                               <text   hint-align='{LangB}'>{body}</text>
                             </subgroup>
                            </group>     
                        </binding>
                    </visual>
               </toast>";

            var _toastXml = $@"<toast>
                                <visual>
                              
                                 <binding template=""ToastGeneric"">
                                <image placement='appLogoOverride' hint-crop='circle' src='{image}' />
                                    <text>{title}</text>
                                    <text>{body}</text>
                                 </binding>
                                </visual>
                              </toast>";
            var doc = new XmlDocument();

            doc.LoadXml(_toastXml);

            var toast = new ToastNotification(doc);
            ToastNotificationManager.CreateToastNotifier(appId).Show(toast);
        }
    }
}

// Example of using it:
// notifi_pip.exe --title "YOUR_TEXT" --body "YOUR_BODY_TEXT" --image "YOUR_IMAGE_PATH" --appname "APP_ID_YOU_CAN_GET_IT_WITH_POWERSHELL"

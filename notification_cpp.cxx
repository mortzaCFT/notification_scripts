// This is cpp version, witch i removed some codes in it,..For simplied...
// also dont forgot to install winrt and Windows ui notification with nuget package in vs.
// Writed by me, mortzaCFT.

#include <iostream>
#include <string>
#include <Windows.h>
#include <winrt/base.h>
#include <winrt/Windows.UI.Notifications.h>
#include <winrt/Windows.Data.Xml.Dom.h>

using namespace winrt;
using namespace Windows::UI::Notifications;
using namespace Windows::Data::Xml::Dom;

void SendToastNotification(const std::wstring& title, const std::wstring& message) {
    winrt::init_apartment();

    // Toast notificaiton with XML..
    std::wstring xmlPayload = LR"(<toast><visual><binding template="ToastGeneric"><text>)" + title + LR"(</text><text>)" + message + LR"(</text></binding></visual></toast>)";
    XmlDocument doc;
    doc.LoadXml(xmlPayload);

    ToastNotification toast(doc);

    auto notifier = ToastNotificationManager::CreateToastNotifier();
  
    notifier.Show(toast);
}

int main() {
    std::wstring title, message;

    std::wcout << L"Title: ";
    std::getline(std::wcin, title);

    std::wcout << L"Body: ";
    std::getline(std::wcin, message);

    SendToastNotification(title, message);
}

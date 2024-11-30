<p align="center">
<image src='https://github.com/user-attachments/assets/73a753d8-a439-488a-ad1d-5fab98640c8c' width="650px"/>
</p>

<h3 align="center">QR Grabber</h3>
<p align="center">A tool to quickly scan qrcodes from screens</p>

<p align="center">
    <a href="#-features"><kbd>🔥 Features</kbd></a>
    <a href="#%EF%B8%8F-installation"><kbd>⚒️ Installation</kbd></a>
    <a href="#-visuals"><kbd>👀 Visuals</kbd></a>
    <a href="#%EF%B8%8F-download-links" target="_blank"><kbd>⬇️ Download Links</kbd></a>
    <a href="">
</p>

<p align="center">
<a href="https://github.com/zingzy/qr-grabber/releases/latest"><img src="https://img.shields.io/github/v/release/zingzy/qr-grabber?logo=github" alt="GitHub release"></a>
<img src="https://img.shields.io/github/downloads/zingzy/qr-grabber/total?logo=github" alt="GitHub all releases">
<img src="https://img.shields.io/github/commit-activity/m/zingzy/qr-grabber?logo=github" alt="GitHub commit activity">
<img src="https://img.shields.io/github/actions/workflow/status/zingzy/qr-grabber/github-ci.yaml" alt="Build Status">
<a href="https://spoo.me/discord"><img src="https://img.shields.io/discord/1192388005206433892?logo=discord" alt="Discord"></a>
</p>

## ⚡ Introduction
QR Grabber is a Python application designed to quickly capture and decode QR codes from your screen. It uses a snipping tool to select the screen area, processes the captured image to detect QR codes, and copies the decoded data to the clipboard.

## ✨ Features

- 🎯 **Quick Screen Capture**: Precise area selection with intuitive snipping tool
- 🔍 **Smart QR Detection**: Fast and accurate QR code scanning and decoding
- 📋 **Instant Clipboard Access**: Decoded data automatically copied to clipboard
- ⌨️ **Global Hotkey**: Quick access with `Ctrl+Alt+Q` system-wide shortcut
- 🔧 **System Tray Integration**: Always ready when you need it

## 🛠️ Installation

### Method 1: Using Pre-built Binary
Download and run the latest release from the [Download Links](#%EF%B8%8F-download-links) section.

### Method 2: From Source
1. Clone the repository:
    ```sh
    git clone https://github.com/zingzy/qr-screen-grabber.git
    cd qr-grabber
    ```

2. Install dependencies:
    ```sh
    pip install poetry
    poetry install
    ```

## 🚀 Usage

1. Launch QR Grabber:
   - From binary: Run the downloaded executable
   - From source: `python main.py`

2. Press `Ctrl+Alt+Q` or use the system tray icon to activate
3. Select screen area containing QR code
4. Decoded content is automatically copied to clipboard

## 🎯 Use Cases

- 📡 **Webinars & Online Events**: Quickly grab links from QR codes displayed during virtual meetings or live streams.
- 🎥 **YouTube Videos**: Scan QR codes shown in video content to access resources or offers.
- 🛜 **Wi-Fi & Login Credentials**: Easily decode and save Wi-Fi passwords or app login details.
- 📇 **Business Contacts**: Extract contact information from QR codes on business cards or websites.
- 🎫 **Event Info**: Capture event QR codes to view schedules, maps, or attendee details.
- 🛍️ **Product Details**: Scan QR codes on packaging to access manuals, reviews, or discounts.
- 🌟 **...and many more!**

## ⬇️ Download Links

<table>
  <tr>
    <td width="70%">
      <b>Download the latest stable version from Github Releases.</b>
    </td>
    <td width="30%">
      <a href="https://github.com/Zingzy/qr-grabber/releases/latest"><img src="https://i.imgur.com/ydZp1wW.png"/></a>
    </td>
  </tr>
</table>

## 🚀 Try It Now

You can scan all these QR codes using **QR Grabber**!

1. **Install the tool** using the download link above.
2. Run the exe.
3. Press **`Ctrl + Alt + Q`** to activate the snipping tool.
4. Select the area of your screen containing a QR code.
5. Check if the decoded value matches the expected value below.

### 🧪 Test QR Codes

<table align="center">
  <thead>
    <tr>
      <th>QR Code</th>
      <th>Expected Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/Zingzy/qr-grabber/refs/heads/main/readme-assets/test-qr-1.png" alt="QR Code 1" width=220></td>
      <td align="center">https://example.com</td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/Zingzy/qr-grabber/refs/heads/main/readme-assets/test-qr-2.png" alt="QR Code 2" width=220></td>
      <td align="center">Hello, QR Grabber!</td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/Zingzy/qr-grabber/refs/heads/main/readme-assets/test-qr-3.png" alt="QR Code 3" width=220></td>
      <td align="center">WiFi:MyNetwork;PWD:123456;</td>
    </tr>
  </tbody>
</table>

## 🤝 Contributing

**Contributions are always welcome!** 🎉 Here's how you can contribute:

- Bugs are logged using the github issue system. To report a bug, simply [open a new issue](https://github.com/zingzy/qr-grabber/issues/new).
- Make a [pull request](https://github.com/zingzy/qr-grabber/pull) for any feature or bug fix.

> [!IMPORTANT]
> For any type of support or queries, Feel free to reach out to us on our <kbd>[discord server](https://spoo.me/github)</kbd>

## 🙏 Acknowledgements

- [Pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar): High-performance QR code decoding library.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Built-in Python library for creating GUI applications.
- [Loguru](https://github.com/Delgan/loguru): Elegant logging framework.
- [Icons8](https://icons8.com/): For providing the high-quality app icon.

---

<h6 align="center">
<img src="https://avatars.githubusercontent.com/u/90309290?v=4" height=30 title="zingzy Copyright">
<br>
© zingzy . 2024

All Rights Reserved</h6>

<p align="center">
	<a href="https://github.com/zingzy/qr-grabber/blob/master/LICENSE.txt"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>

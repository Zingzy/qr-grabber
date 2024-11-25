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
<img src="https://img.shields.io/github/last-commit/zingzy/qr-grabber?logo=github" alt="GitHub last commit">
<img src="https://img.shields.io/github/commit-activity/m/zingzy/qr-grabber?logo=github" alt="GitHub commit activity">
<img src="https://img.shields.io/github/issues/zingzy/qr-grabber?logo=github" alt="GitHub issues">
<img src="https://img.shields.io/github/actions/workflow/status/zingzy/qr-grabber/github-ci.yaml" alt="Build Status">
<a href="https://spoo.me/discord"><img src="https://img.shields.io/discord/1192388005206433892?logo=discord" alt="Discord"></a>
</p>



## ⚡ Introduction
QR Grabber is a Python application designed to quickly capture and decode QR codes from your screen. It uses a snipping tool to select the screen area, processes the captured image to detect QR codes, and copies the decoded data to the clipboard.

## ✨ Features

- **Screen Capture**: Easily select the area of the screen containing the QR code.
- **QR Code Detection**: Detects and decodes QR codes from the captured image.
- **Clipboard Integration**: Automatically copies the decoded data to the clipboard.
- **Keyboard Shortcuts**: Quickly access the snipping tool the keyboard shortcut `Ctrl+Alt+Q`.
- **System Tray Integration**: Conveniently access the application from the system tray.

## 🛠️ Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/zingzy/qr-screen-grabber.git
    cd qr-grabber
    ```

2. Install the dependencies:
    ```sh
    pip install poetry
    poetry install
    ```

## 🚀 Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Use the keyboard shortcut `Ctrl+Alt+Q` to activate the snipping tool.
3. Select the area of the screen containing the QR code.
4. The decoded data will be copied to your clipboard automatically.

## ⬇️ Download Links

<table>
  <tr>
    <td width="70%">
      <b>The stable version of the app is available at Github Releases.</b>
    </td>
    <td width="30%">
      <a href="https://github.com/Zingzy/qr-grabber/releases/latest"><img src="https://i.imgur.com/ydZp1wW.png"/></a>
    </td>
  </tr>
</table>

## 🤝 Contributing

**Contributions are always welcome!** 🎉 Here's how you can contribute:

- Bugs are logged using the github issue system. To report a bug, simply [open a new issue](https://github.com/zingzy/qr-grabber/issues/new).
- Make a [pull request](https://github.com/zingzy/qr-grabber/pull) for any feature or bug fix.

> [!IMPORTANT]
> For any type of support or queries, feel free to reach out to us out on our <kbd>[discord server](https://spoo.me/github)</kbd>

## 🙏 Acknowledgements

- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar/) for QR code detection.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the user interface.
- [Loguru](https://github.com/Delgan/loguru) for logging.

---


<h6 align="center">
<img src="https://avatars.githubusercontent.com/u/90309290?v=4" height=30 title="zingzy Copyright">
<br>
© zingzy . 2024

All Rights Reserved</h6>

<p align="center">
	<a href="https://github.com/zingzy/qr-grabber/blob/master/LICENSE.txt"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>

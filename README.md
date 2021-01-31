# Spotify RGB Sync


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
![GitHub](https://img.shields.io/github/license/FlameOfIgnis/spotify-sync?style=for-the-badge)
[![LinkedIn][linkedin-shield]][linkedin-url]
![Twitter Follow](https://img.shields.io/twitter/follow/ahakcil?style=for-the-badge)


<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Spotify RGB Sync</h3>

  <p align="center">
   Sync RGB devices with Spotify's currently playing songs album cover.
    <br />
    <a href="https://youtu.be/zyYRLC5fsEk">View Demo</a>
    ·
    <a href="https://github.com/FlameOfIgnis/spotify-sync/issues">Report Bug</a>
    ·
    <a href="https://github.com/FlameOfIgnis/spotify-sync/pulls">Add a Bug</a>
  </p>
  Huge thanks to [Layle](https://github.com/ioncodes) for the inspiration.
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Okay now, hear me out. If you are reading this, you probably have a gaming laptop in your hands that is spewing out of the every possible surface of it, and you probably thought it would look really good if you got yourself an RGB headset or mouse or something, and now 
you have a rainbow mess in your hands.

### Built With

* Python. 
* My hours that were supposed to be spent studying for my finals.


## Getting Started

You can take a look at the config.py file to customize your setup a bit, but you can just run it with `python3 -m spotify_sync` (after setting up the configurations of course)

### Prerequisites

* VB-Cable, obtainable [here](https://vb-audio.com/Cable/index.htm).
* For ECIO drivers, you need to copy ECIO.dll and ECIO.sys to the `modules/ecio_rgb/` (you can find them in your oem software's directory, for example, in EVOO Control Center's folders.)
* Windows. Currently only works with Windows. (Sorry *nix friends)

PS: If you are having trouble installing pyaudio, use pipwin instead of pip.

### Installation

1. Download VB-Cable, and follow the steps at audio_loopback's installation [here](https://github.com/FlameOfIgnis/audio_loopback)

2. Get an API key from [Spotify dashboard](https://developer.spotify.com/dashboard/applications), and add it to the `config.py`
3. Clone the repo
   ```sh
   git clone https://github.com/FlameOfIgnis/spotify-sync
   ```
4. Start
   ```sh
   python3 -m spotify-sync
   ```


<!-- CONTRIBUTING -->
## Contributing

If you have a device that this project doesn't support, and you'd like to contribute, you can probably extend one of the modules to support it too. Or you know, just add a new module too.



<!-- LICENSE -->
## License
Distibuted under do whatever you want with this repository license.

<!-- CONTACT -->
## Contact
Twitter - [@ahakcil](https://twitter.com/ahakcil)




[contributors-shield]: https://img.shields.io/github/contributors/FlameOfIgnis/spotify-sync.svg?style=for-the-badge
[contributors-url]: https://github.com/FlameOfIgnis/spotify-sync/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FlameOfIgnis/spotify-sync.svg?style=for-the-badge
[forks-url]: https://github.com/FlameOfIgnis/spotify-synce/network/members
[stars-shield]: https://img.shields.io/github/stars/FlameOfIgnis/spotify-sync.svg?style=for-the-badge
[stars-url]: https://github.com/FlameOfIgnis/spotify-sync/stargazers
[issues-shield]: https://img.shields.io/github/issues/FlameOfIgnis/spotify-sync.svg?style=for-the-badge
[issues-url]: https://github.com/FlameOfIgnis/spotify-sync/issues
[license-shield]: https://img.shields.io/github/license/FlameOfIgnis/spotify-sync.svg?style=for-the-badge
[license-url]: https://github.com/FlameOfIgnis/spotify-sync/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ata-hakcil/
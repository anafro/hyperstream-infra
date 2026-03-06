# Hyperstream Event List

<!--toc:start-->
- [Hyperstream Event List](#hyperstream-event-list)
  - [List](#list)
    - [Clients](#clients)
      - [`client.connect` and `client.disconnect`](#clientconnect-and-clientdisconnect)
    - [Songs](#songs)
      - [`song.download`](#songdownload)
      - [`song.downloading`](#songdownloading)
      - [`song.downloaded`](#songdownloaded)
      - [`song.download.fail`](#songdownloadfail)
      - [`song.get-download-metadata`](#songget-download-metadata)
      - [`song.got-download-metadata`](#songgot-download-metadata)
    - [Song Meta](#song-meta)
      - [`songmeta` type](#songmeta-type)
      - [`songmeta.find`](#songmetafind)
      - [`songmeta.found`](#songmetafound)
      - [`songmeta.select-all`](#songmetaselect-all)
      - [`songmeta.selected-all`](#songmetaselected-all)
<!--toc:end-->

**Hyperstream** parts emit a bunch of events.
To know more about the Hyperstream event system, [click here check out a dedicated document](https://github.com/anafro/hyperstream-infra/blob/main/EVENTSYSTEM-SPEC.md).

## List

Here's a list that describes the content of each event.

> [!NOTE]
> The header of each event type is always the same.
> Hence, in the description, only `content` is described.
> To check out what header, and content are, and what data
> can you get from it, [check out documentation on event structure](https://github.com/anafro/hyperstream-infra/blob/main/EVENTSYSTEM-SPEC.md).

### Clients

> [!NOTE]
> Clients and users are different terms!
> Clients describe Websocket connections,
> whereas users describe real people registered on the website.
> For example, one user can have a phone, and a PC,
> and have the website opened - here, there is one user, and 2 clients.

### Songs

#### `song` type

- `int id` - The song ID;
- `str author` - The author of the song;
- `str title` - The title of the song;
- `int length` - The song length in seconds;

#### `song.download`

- `str query` - The song request that needs to be downloaded;

#### `song.downloaded`

- `...songmeta` - The song that has been downloaded;

#### `song.download.fail`

- `str message` - The message describing what went wrong;

#### `song.expose`

- `int id` - The song id that needs to be exposed;

#### `song.exposed`

- `str url` - The temporary URL to download the song file;
- `...songmeta` - The song that has been exposed;

#### `song.list`

*(A signal)*

#### `song.listed`

- `songmeta[]` - All the songs exist;

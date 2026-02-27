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

#### `client.connect` and `client.disconnect`

*(Header only)*

### Songs

#### `song.download`

- `str query` - The song request that needs to be downloaded;

#### `song.downloading`

- `int id` - The song id that being downloading;
- `int percent` - The percentage of download made;

#### `song.downloaded`

- `int id` - The song id that has been downloaded;

#### `song.download.fail`

- `int id` - The song id that has been failed to downloaded;
- `str message` - The message describing what went wrong;

#### `song.get-download-metadata`

*(Header only)*

#### `song.got-download-metadata`

- `str author` - The author of the song;
- `str title` - The title of the song;

### Song Meta

#### `songmeta` type

- `int id` - The song ID;
- `str author` - The author of the song;
- `str title` - The title of the song;

#### `songmeta.find`

- `int id` - The song ID;

#### `songmeta.found`

- `...songmeta` - The song defined by the ID;

#### `songmeta.select-all`

*(Header only)*

#### `songmeta.selected-all`

- `songmeta[] songs` - All song meta;

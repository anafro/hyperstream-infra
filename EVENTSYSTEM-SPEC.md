# Hyperstream Events

**Hyperstream** infrastructure [is event-driven](https://en.wikipedia.org/wiki/Event-driven_architecture).
It means that service-to-service, as well as client-server communication use events.

This documentation explains the structure of Hyperstream events.

## Terminology

For **Hyperstream**, all verbs meaning *dispatching* events (send, dispatch, emit, issue, etc.),
and verbs meaning *listening to* events (consume, receive, handle etc.)
are used interchangeably.

## Event versioning

For this moment, events do not have versionings.
Effectively, all the events now are v1 events.
If a major update arrives that might change structure,
presentation formats, naming, etc., there may be
versioning introduced. Hence, everything following is for v1,
until event versioning will be introduced.

## Event exchange

All events exchanges between **event nodes**.
An event note is simply anything in the infrastructure
that may receive or/and send events.

## Events structure

All event binaries are JSON objects.
Each event MUST follow the structure below:

```json
{
    "header": {
        "happenedAt": 1772164721531,
        "sid": "gT3scE519cCedkgaddGd", // (optional)
    },
    "content": {
        // Event-related fields
    }
}
```

The JSON consists of two parts: header, and content:

* **Header** is metadata of the event. Any data that is not related
  to the concrete event MUST go to the header.

* **Content** is data of the concrete event type providing details about
  what happened, e.g. if the event related to user, it should likely
  contain user data, like name, ids etc.

> [!CAUTION]
> If you need to change the event, you MUST create a new type or version of the event
> but MUST NOT add those to header, and MUST NOT change/add/remove required content fields.

## Event proxy

To make clients aware want is going on, and also let them perform actions,
there's an event proxy that works over [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) with the power of [socket.io](https://socket.io/).

So, an **event proxy** passes events from server to client, and, naturally, from client to server.

![Hyperstream Proxy Structure](https://raw.githubusercontent.com/anafro/anafro/refs/heads/main/Banners/Hyperstream-Proxy.png)

## Event naming

**Event names** consist of three parts:

* Model/Domain (e.g. song) is what event is related to;
* Action (e.g. download) is what should happen, happening, or happened;
* Detail (optional, e.g. fail) if provided, represents a different event related to base.

All three separated by a dot `.`, and MUST be in kebab case, like CSS properties.
But it is recommended to keep each a single word though.

### Action verb tenses

The action can be:

* *Request event* tells that someone needs to do something (e.g. `song.download`);
* *Process event* tells that someone who received a request event made progress on the request (e.g. `song.downloading`);
* *Completion event* tells that someone who received a request event done doing what request was about (e.g. `song.downloaded`);

As you could notice:

* *Request action verbs* are in Present Simple
* *Request action verbs* are in Present Continuous
* *Request action verbs* are in Present Perfect, without have/has been

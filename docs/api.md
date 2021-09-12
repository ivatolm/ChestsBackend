# Table of Contents

- [CreateRoom](#createroom)
- [JoinRoom](#joinroom)
- [State](#state)
- [Take](#take)
- [Pull](#pull)
- [Ready](#ready)

# CreateRoom

## Description

Used to create a new room.

## Request

**URL**: `/api/createRoom`

**Method**: `POST`

**Parameters**:

```json
{
  "room_settings": "[Structure<RoomSettings>]"
}
```

**Response**:

```json
{
  "room_id": "[String<UUID4>]"
}
```

## Example

**Request**:

```json
{
  "room_settings": {
    "name": "Development room",
    "players_count": 2
  }
}
```

**Response**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10"
}
```

# JoinRoom

## Description

Used to join a room.

## Request

**URL**: `/api/joinRoom`

**Method**: `POST`

**Parameters**:

```json
{
  "room_id": "[String<UUID4>]",
  "nickname": "[String]"
}
```

**Response**:

```json
{
  "player_id": "[String<UUID4>]"
}
```

## Example

**Request**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10",
  "nickname": "Developer"
}
```

**Response**:

```json
{
  "player_id": "8621eba8-03a4-4efe-a0a3-4fd313e9b7b5"
}
```

# State

## Description

Used to get current game state.

## Request

**URL**: `/api/state`

**Method**: `POST`

**Parameters**:

```json
{
  "room_id": "[String<UUID4>]",
  "player_id": "[String<UUID4>]"
}
```

**Response**:

```json
{
  "turn": "[Bool]",
  "cards": "[List<Integer>]"
}
```

## Example

**Request**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10",
  "player_id": "8621eba8-03a4-4efe-a0a3-4fd313e9b7b5"
}
```

**Response**:

```json
{
  "turn": 0,
  "cards": []
}
```

# Take

## Description

Used to take card from another player.

## Request

**URL**: `/api/take`

**Method**: `POST`

**Parameters**:

```json
{
  "room_id": "[String<UUID4>]",
  "player_id": "[String<UUID4>]",
  "nickname": "[String]",
  "card": "[Integer]"
}
```

**Response**:

```json
{
  "success": "[Bool]"
}
```

## Example

**Request**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10",
  "player_id": "8621eba8-03a4-4efe-a0a3-4fd313e9b7b5",
  "nickname": "Alise",
  "card": 4
}
```

**Response**:

```json
{
  "success": 1
}
```

# Pull

## Description

Used to pull card from the deck.

## Request

**URL**: `/api/pull`

**Method**: `POST`

**Parameters**:

```json
{
  "room_id": "[String<UUID4>]",
  "player_id": "[String<UUID4>]"
}
```

**Response**:

```json
{
  "success": "[Bool]"
}
```

## Example

**Request**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10",
  "player_id": "8621eba8-03a4-4efe-a0a3-4fd313e9b7b5"
}
```

**Response**:

```json
{
  "success": 1
}
```

# Ready

## Description

Used to mark player as ready.

## Request

**URL**: `/api/ready`

**Method**: `POST`

**Parameters**:

```json
{
  "room_id": "[String<UUID4>]",
  "player_id": "[String<UUID4>]"
}
```

**Response**:

```json
{
  "success": "[Bool]"
}
```

## Example

**Request**:

```json
{
  "room_id": "7bbe81ec-d15f-451d-92bf-6edd9dfc4c10",
  "player_id": "8621eba8-03a4-4efe-a0a3-4fd313e9b7b5"
}
```

**Response**:

```json
{
  "success": 1
}
```

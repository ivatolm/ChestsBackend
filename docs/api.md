# Table of Contents

- [CreateRoom](#createroom)
- [JoinRoom](#joinroom)
- [GetState](#getstate)
- [TakeCard](#takecard)
- [SetReady](#setready)

# CreateRoom
Description: Used to create a new room. <br>
Request:
  - URL: `/api/createRoom`
  - Method: `POST`
  - Parameters:
    ```json
    {
      "room_settings": {
        "name": String,
        "players_count": Number
      }
    }
    ```
  - Response:
    ```json
    {
      "room_id": String
    }
    ```

# JoinRoom
Description: Used to join a room. <br>
Request:
  - URL: `/api/joinRoom`
  - Method: `POST`
  - Parameters:
    ```json
    {
      "room_id": String,
      "nickname": String
    }
    ```
  - Response:
    ```json
    {
      "player_id": String,
      "room_settings": {
        "name": String,
        "players_count": Number
      }
    }
    ```

# GetState
Description: Used to get current state of a game. <br>
Request:
  - URL: `/api/getState`
  - Method: `POST`
  - Parameters:
    ```json
    {
      "player_id": String
    }
    ```
  - Response:
    ```json
    {
      "cards": List(Number),
      "turn": Number,
      "players": List(
        {
          "nickname": String,
          "ready": Number,
          "cards_count": Number
        }
      )
    }
    ```

# TakeCard
Description: Used to take a card from another player. <br>
Request:
  - URL: `/api/takeCard`
  - Method: `POST`
  - Parameters:
    ```json
    {
      "player_id": String,
      "target_index": Number,
      "card": Number
    }
    ```
  - Response:
    ```json
    {
      "status": Number
    }
    ```

# SetReady
Description: Used to mark requesting player as ready. <br>
Request:
  - URL: `/api/setReady`
  - Method: `POST`
  - Parameters:
    ```json
    {
      "player_id": String
    }
    ```
  - Response:
    ```json
    {
      "status": Number
    }
    ```
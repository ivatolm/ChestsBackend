# Table of Contents

- [CreateRoom](#createroom)
- [JoinRoom](#joinroom)
- [GetState](#getstate)
- [GiveCard](#givecard)
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
      "error_code": Number,
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
      "error_code": Number,
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
      "error_code": Number,
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

# GiveCard
Description: Used to give a card to another player. <br>
Request:
  - URL: `/api/giveCard`
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
      "error_code": Number,
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
      "error_code": Number,
      "status": Number
    }
    ```

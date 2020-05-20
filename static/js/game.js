const request_and_render = async (url) => {
    try {
        response = await fetch(url)

        if (response.ok) {
            game_state = await response.json()
            render(game_state)
        }
    } catch (err) {
        console.error(err)
    }
}

const create_game = async () => {
    request_and_render('/create')
}

const set_piece = async (location) => {
    request_and_render(`/set_piece/${location}`)
}

const render = (game) => {
    // Cool text for the winning player!
    banner = document.getElementById('win_banner')
    if(game.end_condition == 'DRAW') {
        banner.innerHTML = "It's a draw! Try again?"
    } else if (game.end_condition == 'PLAYER_WIN') {
        banner.innerHTML = `Player ${game.current_move} wins!`
    } else {
        banner.innerHTML = ''
    }

    // Find the right cell and add a button to set a piece!
    for( key in game.state) {
        cell = document.getElementById(key)
        if(game.state[key] == null) {
            cell.innerHTML = `<button onclick="set_piece('${key}')">${key}</button>`
        }
        else {
            cell.innerHTML = `&nbsp;${game.state[key]}&nbsp;`
        }
    }
}

window.create_game = create_game
window.set_piece = set_piece
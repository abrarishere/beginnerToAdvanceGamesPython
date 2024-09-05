const readline = require("readline");

// Clears the console in the CLI
function clearConsole() {
  console.clear();
}

// Print the current state of the board
function printBoard(board) {
  clearConsole();
  board.forEach((row) => {
    console.log("+----".repeat(row.length) + "+");
    console.log(
      "|" + row.map((num) => ` ${num === 0 ? " " : num}  `).join("|") + "|",
    );
  });
  console.log("+----".repeat(board[0].length) + "+");
}

// Initialize the board with two random tiles
function initializeBoard() {
  const board = Array.from({ length: 4 }, () => Array(4).fill(0));
  addRandomTile(board);
  addRandomTile(board);
  return board;
}

// Add a random tile (2 or 4) to an empty cell
function addRandomTile(board) {
  const emptyCells = [];
  for (let r = 0; r < 4; r++) {
    for (let c = 0; c < 4; c++) {
      if (board[r][c] === 0) emptyCells.push([r, c]);
    }
  }

  if (emptyCells.length === 0) return false;

  const [row, col] = emptyCells[Math.floor(Math.random() * emptyCells.length)];
  board[row][col] = Math.random() < 0.9 ? 2 : 4;
  return true;
}

// Rotate the board 90 degrees clockwise
function rotateBoard(board) {
  const newBoard = Array.from({ length: 4 }, () => Array(4).fill(0));
  for (let r = 0; r < 4; r++) {
    for (let c = 0; c < 4; c++) {
      newBoard[c][3 - r] = board[r][c];
    }
  }
  return newBoard;
}

// Handle left move logic
function moveLeft(board) {
  function merge(row) {
    const newRow = row.filter((val) => val !== 0);
    for (let i = 0; i < newRow.length - 1; i++) {
      if (newRow[i] === newRow[i + 1]) {
        newRow[i] *= 2;
        newRow[i + 1] = 0;
      }
    }
    const mergedRow = newRow.filter((val) => val !== 0);
    return mergedRow.concat(Array(4 - mergedRow.length).fill(0));
  }

  return board.map((row) => merge(row));
}

// Handle right move logic
function moveRight(board) {
  return board.map((row) => moveLeft([row.reverse()])[0].reverse());
}

// Handle up move logic
function moveUp(board) {
  const rotated = rotateBoard(board);
  return rotateBoard(rotateBoard(rotateBoard(moveLeft(rotated))));
}

// Handle down move logic
function moveDown(board) {
  const rotated = rotateBoard(board);
  return rotateBoard(rotateBoard(rotateBoard(moveRight(rotated))));
}

// Check if the game is over (no moves left)
function checkGameOver(board) {
  for (const row of board) {
    if (row.includes(0)) return false;
  }

  for (let r = 0; r < 4; r++) {
    for (let c = 0; c < 3; c++) {
      if (board[r][c] === board[r][c + 1] || board[c][r] === board[c + 1][r]) {
        return false;
      }
    }
  }

  return true;
}

// Main game loop
async function main() {
  let board = initializeBoard();

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  while (true) {
    printBoard(board);

    const move = await new Promise((resolve) => {
      rl.question("Move (w/a/s/d): ", resolve);
    });

    if (!["w", "a", "s", "d"].includes(move)) {
      console.log("Invalid move. Use w, a, s, or d.");
      continue;
    }

    let newBoard;
    if (move === "w") newBoard = moveUp(board);
    else if (move === "a") newBoard = moveLeft(board);
    else if (move === "s") newBoard = moveDown(board);
    else if (move === "d") newBoard = moveRight(board);

    if (JSON.stringify(newBoard) !== JSON.stringify(board)) {
      board = newBoard;
      if (!addRandomTile(board)) {
        printBoard(board);
        console.log("Game Over!");
        break;
      }
    } else if (checkGameOver(board)) {
      printBoard(board);
      console.log("Game Over!");
      break;
    }
  }

  rl.close();
}

// Run the main game loop
main();

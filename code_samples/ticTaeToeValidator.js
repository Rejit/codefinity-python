function validateBoard(board) {
    // Constantes
    const INVALID = 'invalid';
    const TIE = 'tie';
    const a = 'a';
    const b = 'b';

    // =========================
    // Piece count validation
    // =========================
    let countA = 0;
    let countB = 0;
    for (const row of board) {
        for (const cell of row) {
            if (cell === a) countA++;
            if (cell === b) countB++;
        }
    }

    // A siempre inicia
    const diff = countA - countB;
    if (diff < 0 || diff > 1) return INVALID;

    // =========================
    // Winner detection
    // =========================
    // Todas las posibles líneas ganadoras
    const lines = [
        [[0, 0], [0, 1], [0, 2]], // row1
        [[1, 0], [1, 1], [1, 2]], // row2
        [[2, 0], [2, 1], [2, 2]], // row3
        [[0, 0], [1, 0], [2, 0]], // col1
        [[0, 1], [1, 1], [2, 1]], // col2
        [[0, 2], [1, 2], [2, 2]], // col3
        [[0, 0], [1, 1], [2, 2]], // diag1
        [[0, 2], [1, 1], [2, 0]], // diag2
    ];
    const hasWon = (player) => lines.some(line => line.every(([r, c]) => board[r][c] === player));
    const aWins = hasWon(a);
    const bWins = hasWon(b);

    // =========================
    // Invalid board states
    // =========================

    // Ambos ganan al mismo tiempo
    if (aWins && bWins) return INVALID;

    // Si gana A debe tener exactamente una jugada más
    if (aWins && diff !== 1) return INVALID;

    // Si gana B deben tener el mismo número de jugadas
    if (bWins && diff !== 0) return INVALID;

    // =========================
    // Result
    // =========================
    if (aWins) return a;
    if (bWins) return b;

    return TIE;
}

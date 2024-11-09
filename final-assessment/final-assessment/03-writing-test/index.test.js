import { sum } from './index.js';
import { test } from 'node:test';
import assert from 'node:assert';

const ans = sum(5,4);
console.log(ans)

test('should add correctly',()=> {
    const operandA = 5;
    const operandB = 4;

    const actualValue = sum(operandA,operandB);

    const expectedValue = 9;
    assert.equal(actualValue,expectedValue);
});
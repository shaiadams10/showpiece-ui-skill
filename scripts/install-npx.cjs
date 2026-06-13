#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

function parseArgs(argv) {
  const args = {
    target: process.cwd(),
    skipAntigravityCliMirror: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--") {
      continue;
    } else if (arg === "--target" || arg === "-t") {
      args.target = argv[i + 1];
      i += 1;
    } else if (arg === "--skip-antigravity-cli-mirror") {
      args.skipAntigravityCliMirror = true;
    } else if (arg === "--help" || arg === "-h") {
      args.help = true;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

function printHelp() {
  console.log(`animated-showcase-ui-skill installer

Usage:
  npx github:shaiadams10/animated-showcase-ui-skill
  npx github:shaiadams10/animated-showcase-ui-skill -- --target /path/to/project

Options:
  -t, --target <dir>                 Target project root. Defaults to cwd.
  --skip-antigravity-cli-mirror      Do not create .agent/skills mirror.
  -h, --help                         Show this help.
`);
}

function copyDirectory(source, destination) {
  fs.rmSync(destination, { recursive: true, force: true });
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.cpSync(source, destination, { recursive: true });
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    printHelp();
    return;
  }

  const packageRoot = path.resolve(__dirname, "..");
  const sourceSkill = path.join(packageRoot, ".agents", "skills", "animated-showcase-ui");
  const targetRoot = path.resolve(args.target);

  if (!fs.existsSync(path.join(sourceSkill, "SKILL.md"))) {
    throw new Error(`Skill source is missing: ${sourceSkill}`);
  }

  const codexDest = path.join(targetRoot, ".agents", "skills", "animated-showcase-ui");
  copyDirectory(sourceSkill, codexDest);
  console.log("Installed repo-local skill:");
  console.log(`  ${codexDest}`);

  if (!args.skipAntigravityCliMirror) {
    const antigravityCliDest = path.join(targetRoot, ".agent", "skills", "animated-showcase-ui");
    copyDirectory(sourceSkill, antigravityCliDest);
    console.log("Installed Antigravity CLI project mirror:");
    console.log(`  ${antigravityCliDest}`);
  }
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}


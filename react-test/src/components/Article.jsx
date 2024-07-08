import React, { Component } from "react";
import SearchIcon from "@mui/icons-material/Search";
import SchoolIcon from "@mui/icons-material/School";
import SpaIcon from "@mui/icons-material/Spa";
import ComputerIcon from "@mui/icons-material/Computer";
import EmojiEventsIcon from "@mui/icons-material/EmojiEvents";
const projects = [
  {
    title: "SSAFY 1학기 프로젝트 'MEOVA' (2024)",
    description: "Open API를 활용한 검색 중심 영화 추천 기반 SNS 서비스",
    skills: "Python, Django, Vue, ChatGPT",
    link: "https://github.com/cadetbluee/project-meova",
  },
  {
    title: "사이드 프로젝트 미니게임 'PONGDANG' (2024)",
    description:
      "상대의 비치볼을 밀어내라! 육지 위에 마지막까지 살아남는 플레이어가 승자가 되는 전략 알 까기 게임",
    skills: "Python, Pygame, Adobe",
    link: "https://github.com/cadetbluee/project-pongdang",
  },
];

export default class Article extends Component {
  render() {
    return (
      <article>
        <h3>
          <SearchIcon />
          About me
        </h3>
        <ul>
          <li>윤채영 / 항상 최선을 다하는 개발자입니다.</li>
        </ul>
        <h3>
          <SchoolIcon />
          Education & Activity
        </h3>
        <ul>
          <li>Samsung SW academy for youth(SSAFY) 11th(2024.01 ~)</li>
          <li>
            Bachelor's Degree on Molecular & Life Science at Hanyang University
            (2019.03 ~ 2024.02)
          </li>
        </ul>
        <h3>
          <SpaIcon />
          Tech Stack
        </h3>
        <div style={{ display: "flex", alignItems: "flex-start" }}>
          <img
            src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"
            alt="python"
          />
          <img
            src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"
            alt="django"
          />
          <img
            src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"
            alt="mysql"
          />
          <img
            src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"
            alt="html"
          />
          <br />
          <img
            src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"
            alt="css"
          />
          <img
            src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"
            alt="js"
          />
          <img
            src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"
            alt="vue"
          />
        </div>
        <h3>
          <ComputerIcon />
          Projects
        </h3>
        <table align="center">
          <thead>
            <tr>
              <th>Title</th>
              <th>Description</th>
              <th>Skills</th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            {projects.map((project, index) => (
              <tr key={index}>
                <td>{project.title}</td>
                <td>{project.description}</td>
                <td>{project.skills}</td>
                <td>
                  <a
                    href={project.link}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {project.link}
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <h3>
          <EmojiEventsIcon />
          Achievements
        </h3>
        <ul>
          <li>SSAFY 1학기 프로젝트 최우수상</li>
          <li>SSAFY 1학기 성적 우수상</li>
        </ul>
      </article>
    );
  }
}

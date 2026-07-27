import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

export default function Navbar() {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav className="sticky top-0 z-50 flex h-16 items-center border-b border-border bg-bg/85 px-6 backdrop-blur-[16px]">
      <Link
        to="/gallery"
        className="font-heading text-xl tracking-[0.04em] text-accent"
      >
        Clauset5
      </Link>

      <div className="ml-auto flex items-center gap-2">
        {isAuthenticated ? (
          <>
            <Link
              to="/gallery"
              className="rounded-sm px-4 py-2 text-sm uppercase tracking-[0.06em] text-fg-muted transition-colors hover:bg-white/4 hover:text-fg"
            >
              Garderobe
            </Link>
            <Link
              to="/outfits"
              className="rounded-sm px-4 py-2 text-sm uppercase tracking-[0.06em] text-fg-muted transition-colors hover:bg-white/4 hover:text-fg"
            >
              Outfits
            </Link>
            <button
              onClick={handleLogout}
              className="rounded-sm px-4 py-2 text-sm uppercase tracking-[0.06em] text-fg-muted transition-colors hover:bg-white/4 hover:text-fg"
            >
              Logout
            </button>
          </>
        ) : (
          <>
            <Link
              to="/login"
              className="rounded-sm px-4 py-2 text-sm uppercase tracking-[0.06em] text-fg-muted transition-colors hover:bg-white/4 hover:text-fg"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="rounded-sm px-4 py-2 text-sm uppercase tracking-[0.06em] text-fg-muted transition-colors hover:bg-white/4 hover:text-fg"
            >
              Registrieren
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
